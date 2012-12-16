'''
Created on Dec 8, 2012

@author: Salvador Faria
'''

MAX_ROWS = 250

class Image(object):
    """ Simple Image Library - starts on 0x0 cordinates """
    rows = 1
    columns = 1
    matrix = None
    
    def __init__(self, columns=1, rows=1, color=None):
        self.rows = rows
        self.columns = columns
        assert rows < MAX_ROWS, "Maximium rows exceeded!"
        self.matrix = [[color for c in range(columns)] for r in range(rows)]
    
    def clear(self, color):
        self.paintArea((0, self.columns-1, 0, self.rows-1), color)
    
    def getPixelColor(self, pixel):
        col, row = pixel
        return self.matrix[row][col]
    
    def paintPixel(self, pixel, color):
        col, row = pixel
        self.matrix[row][col] = color
        
    def paintArea(self, box, color):
        col1, col2, row1, row2 = box
        for col in range(col1, col2+1):
            for row in range(row1, row2+1):
                self.matrix[row][col] = color
    
    def find_neighbours(self, pixel, color):
        """ Finds all neighours with the same color as the given pixel, 
            and they share a common side.
        """
        area = [pixel] # list of pixels with all neighbours
        work = {pixel: True} # pixels that we need to visit and discover neighbours
        visited = {} # a way to know if a pixel was visited before or not
        
        while len(work) > 0:
            pixel = work.keys()[0]
            
            if pixel not in visited:
                col, row = pixel
                # check for top pixel
                p = (col, row-1)
                if p[1] >= 0 and p[1] <= (self.rows - 1) and self.matrix[p[1]][p[0]] == color:
                    area.append(p)
                    if p not in visited:
                        work[p] = True
                # check for bottom pixel
                p = (col, row+1)
                if p[1] >= 0 and p[1] <= (self.rows - 1) and self.matrix[p[1]][p[0]] == color:
                    area.append(p)
                    if p not in visited:
                        work[p] = True
                # check for left pixel
                p = (col-1, row)
                if p[0] >= 0 and p[0] <= (self.columns - 1) and self.matrix[p[1]][p[0]] == color:
                    area.append(p)
                    if p not in visited:
                        work[p] = True
                # check for right pixel
                p = (col+1, row)
                if p[0] >= 0 and p[0] <= (self.columns - 1) and self.matrix[p[1]][p[0]] == color:
                    area.append(p)
                    if p not in visited:
                        work[p] = True
                
                # "mark" pixel as visited, so we dont go to this pixel again
                visited[pixel] = True
            
            # remove pixel from work structure
            del work[pixel]
        
        # return all neighbours
        return area
    
    def as_string(self):
        return "\n".join(" ".join(c) for c in self.matrix)
    
    def __unicode__(self):
        return "%s\n%s" % (self.__class__.__name__, "\n".join(str(c) for c in self.matrix))
    
    def __str__(self):
        return unicode(self).encode("utf-8")

