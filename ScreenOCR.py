import cv2
from PIL import Image, ImageOps
import pytesseract
import numpy as np
class ScreenTextFinder:
    ACTION_FOUND_NONE = 0
    ACTION_FOUND_TAP = 1
    ACTION_SEARCH_NONE = 10
    ACTION_SEARCH_SWIPE_UP = 11
    ACTION_SEARCH_SWIPE_DOWN = 12
   
    def __init__( self, device, roi = { &quot;X&quot;: 0, &quot;Y&quot;: 0, &quot;width&quot;: 1, &quot;height&quot;: 1
},
                 action_found = 0, action_search = 10,
                 repeats = 3, swipe_range = 0.75, swipe_speed = 100, thresh =
150, DEBUG = False ):
        self.device = device
        self.repeats = repeats
        self.roi = roi
        self.swipe_range = swipe_range
        self.swipe_speed = swipe_speed
        self.action_found = action_found
        self.action_search = action_search
        self.DEBUG = DEBUG
        self.thresh = thresh
       
       
        self.compute_gestures()
       
    def compute_gestures( self ):
        # convert from XYWH to X0Y0X1Y1
        s_x, s_y, s_w, s_h = self.roi[ &#39;X&#39; ], self.roi[ &#39;Y&#39; ], self.roi[ &#39;width&#39;
], self.roi[ &#39;height&#39; ]
        s_x0, s_y0, s_x1, s_y1 = s_x, s_y, s_x + s_w, s_y + s_h
        # generate swipe gestures
        s_cx, s_cy = ( s_x0 + s_x1 ) / 2, 1. - (( s_y0 + s_y1 ) / 2 )
        s_y_span = self.swipe_range
       

        if( self.action_search == ScreenTextFinder.ACTION_SEARCH_SWIPE_UP ):
            self.swipe = dict( end = dict( x = s_cx, y = s_cy - (( s_y_span * s_h
) / 2 )), start = dict( x = s_cx, y = s_cy + (( s_y_span * s_h ) / 2 )) )
        else:
            self.swipe = dict( start = dict( x = s_cx, y = s_cy - (( s_y_span *
s_h ) / 2 )), end = dict( x = s_cx, y = s_cy + (( s_y_span * s_h ) / 2 )) )
       
        self.s_box = ( s_x, s_y, s_w, s_h )
        self.s_corners = ( s_x0, s_y0, s_x1, s_y1 )
        self.s_center = ( s_cx, s_cy )
       
    def apply_swipe( self, swipe, repeats = 1 ):
        self.device.moveStylus( z = 10., **swipe[ &#39;start&#39; ] )
        self.device.robot.setFeedrates( fine = self.swipe_speed, coarse =
self.swipe_speed )
        for i in range( repeats ):
            self.device.swipe( swipe[ &#39;start&#39; ], swipe[ &#39;end&#39; ], lag = 0.1, hold
= 0.1 )
        self.device.robot.setFeedrates( fine = self.swipe_speed, coarse = 500 )
       
    def preprocess_screen_text( self, img ):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ##img = cv2.bitwise_not( img )
        img[np.where(img &gt; self.thresh + 15)] = 255
        img[np.where(img &lt; self.thresh)] = 0
        return img
   
    def find_text( self, img, ref_str=&#39;caller&#39;, debug=False ):
        img = self.preprocess_screen_text(img)
       
        if( self.DEBUG ):
            cv2.imshow(&quot;processed&quot;, img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
       
        tess_img = Image.fromarray(img)#.convert(&#39;L&#39;)
        tess_dict = pytesseract.image_to_data(tess_img, config=r&quot;--oem 3 --psm
11&quot;, output_type=pytesseract.Output.DICT)
        #tess_string = pytesseract.image_to_string(tess_img, config=r&quot;--oem 3 --
psm 11&quot;, output_type=pytesseract.Output.DICT)
        if( self.DEBUG ):
            print(tess_dict[&#39;text&#39;])
        found_positions = []

        found_words = 0
       
        for word in ref_str.split(&quot; &quot;):
            for i, left in enumerate(tess_dict[&#39;left&#39;]):
                top= tess_dict[&#39;top&#39;][i]
                width = tess_dict[&#39;width&#39;][i]
                height = tess_dict[&#39;height&#39;][i]
                if( int(float(tess_dict[&#39;conf&#39;][i])) &gt; 0 and
len(tess_dict[&#39;text&#39;][i]) &gt; 0 ):
                    if( word.lower() in tess_dict[&#39;text&#39;][i].lower() ):
                        found_words += 1
                       
found_positions.append([tess_dict[&#39;left&#39;][i],tess_dict[&#39;top&#39;][i],tess_dict[&#39;width
&#39;][i],tess_dict[&#39;height&#39;][i]])
        if( found_words == len(ref_str.split(&quot; &quot;)) ):
            found_pos = [min(x[0] for x in found_positions), min(x[1] for x in
found_positions), sum(x[2] for x in found_positions), max(x[3] for x in
found_positions)]
           
            img = cv2.circle(img, (found_pos[0]+found_pos[2]//2,
found_pos[1]+found_pos[3]//2), 5, (0, 0, 255), 10)
            found_pos = [ found_pos[0]+found_pos[2]//2,
found_pos[1]+found_pos[3]//2 ]
           
            return found_pos, img
        return [-1,-1], img
   
    def ocr_lookup( self, img, text = &#39;&#39; ):
        results, _ = self.find_text( img, text )
        if( results[0] &gt; 0 ):
            return results
   
    def scan_and_select( self, target_text ):
        # selector patch
        s_x0, s_y0, s_x1, s_y1 = self.s_corners
        s_x, s_y, s_w, s_h = self.s_box
       
        text_position = None
        ocr_it = 0
       
        while( text_position is None and ocr_it &lt; 2 ):
            self.device.screenshot( &#39;selector.jpg&#39; )

            image = cv2.imread( &#39;selector.jpg&#39; )
           
            roi_crop = image
            if( self.roi != { &quot;X&quot;: 0, &quot;Y&quot;: 0, &quot;width&quot;: 1, &quot;height&quot;: 1 } ):  
                img_h, img_w = image.shape[ :2 ]
                c_x0, c_y0, c_x1, c_y1 = int( s_x0 * img_w ), int( s_y0 * img_h
), int( s_x1 * img_w ), int( s_y1 * img_h )
               
                # roi crop
                roi_crop = image[ c_y0:c_y1, c_x0:c_x1 ]
           
            text_position = self.ocr_lookup( roi_crop, target_text )
           
            if( text_position is not None ):
                break
           
            ocr_it += 1
       
        if( text_position is not None ):
            # relative units
            t_x, t_y = text_position
            t_x, t_y = t_x / roi_crop.shape[ 1 ], t_y / roi_crop.shape[ 0 ]
           
            tap_position = dict( x = s_x0 + ( t_x * s_w ), y = 1. - ( s_y0 + (
t_y * s_h ) ) )
            return tap_position
       
        return None
   
    def __call__( self, target_text, roi=None, DEBUG=False, thresh = 150 ):
       
        if( roi != None ):
            self.roi = roi
            self.compute_gestures()
       
        self.DEBUG = DEBUG
        self.thresh = thresh
       
        found = False
        for repeat in range( self.repeats ):
            found = self.scan_and_select( target_text )
           
            if( found is not None ):
                if( self.action_found == ScreenTextFinder.ACTION_FOUND_TAP ):
                    self.device.tap( duration = 0.15, **found )

                else:
                    return found
                break
            elif( self.action_search != ScreenTextFinder.ACTION_SEARCH_NONE ):
                self.apply_swipe( self.swipe )
               
        if not found:
            return None
            #raise Exception( &#39;Cannot find selector option {}&#39;.format( option ) )