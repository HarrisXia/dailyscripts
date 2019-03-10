from pylab import *
from pylab import mpl
# from scipy.interpolate import spline 
def conf_zh(font_name):

    mpl.rcParams['font.sans-serif'] = [font_name]
    mpl.rcParams['axes.unicode_minus'] = False 

conf_zh("Droid Sans Fallback")