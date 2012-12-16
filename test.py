'''
Created on Dec 8, 2012

@author: Salvador Faria
'''
import unittest

class Test(unittest.TestCase):
    editor = None
    matrix = None
     
    def setUp(self):
        from editor import Editor
        self.editor = Editor()
        self.editor.execute_command("I", args=[10, 10])
        self.matrix = self.editor.im.matrix
    
    def test_cmd_I(self):
        e = self.editor
        e.execute_command("I", args=[10, 10])
        
        self.assertEqual(len(self.matrix), 10, "Invalid image dimensions, rows")
        self.assertEqual(len(self.matrix[0]), 10, "Invalid image dimensions, columns")
    
    def test_cmd_L(self):
        e = self.editor
        e.execute_command("L", args=[2, 3, "A"])
        
        # note, convert to 0x0 system, when accessing matrix
        e.execute_command("L", args=[3, 3, "B"])
        self.assertEqual(self.matrix[3-1][2-1], "A", "Invalid pixel color, expecting A")
        
        e.execute_command("L", args=[3, 3, "B"])
        self.assertNotEqual(self.matrix[3-1][3-1], "A", "Invalid pixel color, expecting A")
        self.assertEqual(self.matrix[3-1][3-1], "B", "Invalid pixel color, expecting B")
            
    def test_cmd_V(self):
        e = self.editor
        e.execute_command("V", args=[2, 3, 4, "W"])
                
        self.assertEqual(self.matrix[3-1][2-1], "W", "Invalid pixel color, expecting W")
        self.assertEqual(self.matrix[4-1][2-1], "W", "Invalid pixel color, expecting W")
    
    def test_cmd_H(self):
        e = self.editor
        e.execute_command("H", args=[3, 4, 2, "Z"])
                
        self.assertEqual(self.matrix[2-1][3-1], "Z", "Invalid pixel color, expecting Z")
        self.assertEqual(self.matrix[2-1][4-1], "Z", "Invalid pixel color, expecting Z")
    
    def test_cmd_C(self):
        e = self.editor
        e.execute_command("C")
        for r in self.matrix:
            for c in r:
                self.assertTrue(c == "O", "Clear failed!")    
    
    def test_cmd_F(self):
        e = self.editor
        
        e.execute_command("F", args=[3, 3, "J"])
        self.assertEqual(self.matrix[10-1][10-1], "J", "Invalid pixel color, expecting J")
        self.assertEqual(self.matrix[0][0], "J", "Invalid pixel color, expecting J")
        
    def test_all(self):
        e = self.editor
        
        e.execute_command("C")
        e.execute_command("L", args=[2, 3, "A"])
        e.execute_command("F", args=[3, 3, "J"])
        e.execute_command("V", args=[2, 3, 4, "W"])
        e.execute_command("H", args=[3, 4, 2, "Z"])
        e.execute_command("L", args=[4, 8, "A"])
        
        # check for W
        self.assertEqual(self.matrix[3-1][2-1], "W", "Invalid pixel color, expecting W")
        self.assertEqual(self.matrix[4-1][2-1], "W", "Invalid pixel color, expecting W")
        # check for Z
        self.assertEqual(self.matrix[2-1][3-1], "Z", "Invalid pixel color, expecting Z")
        self.assertEqual(self.matrix[2-1][4-1], "Z", "Invalid pixel color, expecting Z")
        # check for J
        self.assertEqual(self.matrix[10-1][10-1], "J", "Invalid pixel color, expecting J")
        self.assertEqual(self.matrix[0][0], "J", "Invalid pixel color, expecting J")
        # check for A
        self.assertEqual(self.matrix[8-1][4-1], "A", "Invalid pixel color, expecting A")


if __name__ == "__main__":
    unittest.main()

