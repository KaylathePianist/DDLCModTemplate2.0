default AFZoom = True
default AFDim = True

python early:

    # QoL functions
    def iterable(x):
        try:
            iter(x)
            return True
        except:
            return False
        
init -999 python:

    class WarpedTimeProgressTracker:
        def __init__(self, maxTime, warp, minTime=0.0, _progress=0.0):
            assert minTime <= maxTime
            self.minTime = minTime
            self.maxTime = maxTime
            self.warp = warp

            self.done = True if minTime == maxTime or maxTime == 0.0 else False
            self.progress = _progress
            self.warpedProgress = self.progress
        
        @property
        def warpedProgress(self):
            return self._warpedProgress
        
        @warpedProgress.setter
        def warpedProgress(self, value):
            self._warpedProgress = self.warp(value)

        def update(self, dt):
            self.progress += dt
            self.progress = min(self.maxTime, max(self.minTime, self.progress))

            # if self.done: return self.warpedProgress

            complete = self.progress / self.maxTime
            if complete <= 0.0: complete = 0.0
            if complete >= 1.0:
                complete = 1.0
                self.done = True
            else: self.done = False
            
            self.warpedProgress = complete

            return self.warpedProgress
            
        def reset(self):
            self.progress = 0.0
            self.done = False

    class _SimpleAutoFocus(object):        
        def __init__(self, tag, warp, time, zoom, dim):
            self.tag = tag
            self.zoom = zoom
            self.dim = -dim

            if not iterable(warp): warp = (warp, warp)
            else: assert len(warp) == 2
            
            if not iterable(time): time = (time, time)
            else: assert len(time) == 2

            self.zoomTime = WarpedTimeProgressTracker(time[0], warp[0])
            self.dimTime  = WarpedTimeProgressTracker(time[1], warp[1])
        
            self.isTag = False
            self.last_st = 0.0

        def compareTag(self):
            self.isTag = self.tag == renpy.get_say_image_tag()

        def __call__(self, trans, st, at):
            dt = max(at - self.last_st, 1/100)
            self.last_st = at

            self.compareTag()
            if self.isTag:
                ztime = self.zoomTime.update(dt if AFZoom else -dt)
                dtime = self.dimTime.update(dt)
            else:
                ztime = self.zoomTime.update(-dt)
                dtime = self.dimTime.update(-dt if AFDim else dt)

            trans.zoom = 1.0 + (self.zoom - 1.0) * ztime
            trans.matrixcolor = BrightnessMatrix(self.dim * (1.0-dtime))

            return 0.0

    def SimpleAutoFocus(tag, warp=_warper.easein, time=0.15, zoom=1.01 , dim=0.1):
        return Transform(function=_SimpleAutoFocus(tag, warp, time, zoom, dim))
