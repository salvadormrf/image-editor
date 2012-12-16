#! /usr/bin/env python

'''
Created on Dec 8, 2012

@author: Salvador Faria
'''

from editor import Editor

if __name__ == '__main__':    
    
    e = Editor()
    
    cmd = ""
    while cmd != "X":
        args_raw = raw_input('image-editor>>> ').strip()
        args = args_raw.split(" ")
        
        # extract command and respective arguments
        cmd = args[0]
        cmd_args = args[1:]
            
        e.execute_command(cmd, cmd_args)

