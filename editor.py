'''
Created on Dec 8, 2012

@author: Salvador Faria
'''
from image import Image
# TODO use logger instead of print

class Editor(object):
    im = None
    
    def __init__(self):
        pass
    
    def execute_command(self, cmd, args=[]):
        m = getattr(self, "_%s" % cmd, None)
        if m is None or not callable(m):
            print "Invalid command!"   #logger.debug("bla bla bla...")
            return
        
        # call method
        try:
            m(args)
        except Exception as e:
            # logger.exception("bla bla bla...")
            print "Failed to execute command '%s', reason: '%s'" % (cmd, e)
    
    def _I(self, args=[]):
        self.parse_args(args, required_args=[int, int], requires_init=False)
        self.im = Image(args[0], args[1], color="O")
    
    def _C(self, args=[]):
        self.parse_args(args, required_args=[])
        self.im.clear(color="O")
    
    def _L(self, args=[]):
        self.parse_args(args, required_args=[int, int, str])
        x, y, color = args[0], args[1], args[2]
        self.im.paintPixel((x-1, y-1), color=color)
        
    def _V(self, args=[]):
        self.parse_args(args, required_args=[int, int, int, str])
        x, y1, y2, color = args[0], args[1], args[2], args[3]
        self.im.paintArea((x-1, x-1, y1-1, y2-1), color)
    
    def _H(self, args=[]):
        self.parse_args(args, required_args=[int, int, int, str])
        x1, x2, y, color = args[0], args[1], args[2], args[3]
        self.im.paintArea((x1-1, x2-1, y-1, y-1), color)
    
    def _F(self, args=[]):
        self.parse_args(args, required_args=[int, int, str])
        x, y, color = args[0], args[1], args[2]
        pixel_color = self.im.getPixelColor((x-1, y-1))
        area = self.im.find_neighbours((x-1, y-1), pixel_color)    
        for p in area:
            self.im.paintPixel(p, color)
        
    def _S(self, args=[]):
        self.parse_args(args, required_args=[])
        print self.im.as_string()

    def _X(self, args=[]):
        self.parse_args(args, required_args=[], requires_init=False)
        pass
    
    def parse_args(self, args, required_args=[], requires_init=True):
        # TODO convert this function to use as decorator
        """ Verifies if the given args are the same type as expected """
        if len(args) != len(required_args):
            raise Exception("Invalid number of arguments!")
        for i, arg_type in enumerate(required_args):
            # try to convert str to interger when expected integer
            if arg_type is int and isinstance(args[i], str):
                try:
                    args[i] = int(args[i])
                except ValueError:
                    pass
            if not isinstance(args[i], arg_type):
                raise Exception("Invalid argument type! '%s'" % args[i])
            # argument values cannot be less than 1
            if arg_type is int and args[i] <= 0:
                raise Exception("Argument must be bigger than 0! '%s'" % args[i])
            if arg_type is str and len(args[i]) > 1:
                raise Exception("Only one character is allowed! '%s'" % args[i])
            if arg_type is str and args[i].islower():
                raise Exception("Lowecase character not allowed! '%s'" % args[i])
        # check if the image was created, otherwise cannot run some commands
        if requires_init and self.im is None:
            raise Exception("Need to create image first!")

