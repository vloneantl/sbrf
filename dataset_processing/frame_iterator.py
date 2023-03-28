import math
import cv2
from datetime import timedelta

class FramesIterator:
    def __init__(self, filename, from_sec = 0, to_sec = None, span_sec=None, frame_rate=None, raise_frame_exception=False) -> None:
        self.filename = filename
        self.span_sec = span_sec
        self.raise_frame_exception = raise_frame_exception

        self.cap = cv2.VideoCapture(filename)
        if frame_rate:
            self.frame_rate = frame_rate
        else:
            self.frame_rate = self.cap.get(5)

        self.video_frames_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.start_frame = math.ceil(from_sec * self.frame_rate)

        if to_sec:
            self.end_frame = int(to_sec * self.frame_rate)
        else:
            self.end_frame = self.video_frames_count - 1
        
        self.curr_frame = self.start_frame
        self.curr_sec = from_sec

    def __iter__(self):
        return self

    def __next__(self):
        # process video
        if not self.cap.isOpened():
            raise RuntimeError('Reader closed unexpectedly')

        while True:
            curr_frame = self.curr_frame
            if curr_frame <= self.end_frame:
                if self.span_sec:
                    self.cap.set(cv2.CAP_PROP_POS_FRAMES, int(curr_frame))
                try:
                    ret, frame = self.cap.read()
                    if ret != True:
                        e = 'Unexpected end of video'
                        if self.raise_frame_exception:
                            raise RuntimeError(e)
                        print(e)
                        self.cap.release()
                        raise StopIteration
                    
                    frame_time = timedelta(seconds = self.curr_frame / self.frame_rate)

                    if self.span_sec:
                        self.curr_sec += self.span_sec
                        self.curr_frame = math.ceil(self.curr_sec * self.frame_rate)
                    else:
                        self.curr_frame += 1
                        self.curr_sec = self.curr_frame/self.frame_rate

                    return frame, curr_frame, frame_time
                
                except Exception as e:
                    if self.raise_frame_exception:
                        raise Exception
                    print(e)

            self.cap.release()
            raise StopIteration