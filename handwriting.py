# first of all import these modules that are listed and installed them


import pywhatkit as pw

txt = """python is very conveintent language for new programmer and it is often said that 
and also you heard that it is much easy language than other programming language .i
think this words or this sentense is write approximately write.
"""
pw.text_to_handwriting(txt,"demo12.png",[255,0,0])
print(" END ")