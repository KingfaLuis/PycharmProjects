# with context_manager:
#     # 代码块
#     pass
#
# with context_namager as context:
#     pass
#
# with A() as a, B() as b:
#     pass
# with A() as a:
#     with B() as b:
#         pass

class GeneratorContextManager(object):

   def __init__(self, gen):
       self.gen = gen

   def __enter__(self):
       try:
           return self.gen.next()
       except StopIteration:
           raise RuntimeError("generator didn't yield")

   def __exit__(self, type, value, traceback):
       if type is None:
           try:
               self.gen.next()
           except StopIteration:
               return
           else:
               raise RuntimeError("generator didn't stop")
       else:
           try:
               self.gen.throw(type, value, traceback)
               raise RuntimeError("generator didn't stop after throw()")
           except StopIteration:
               return True
           except:
               # only re-raise if it's *not* the exception that was
               # passed to throw(), because __exit__() must not raise
               # an exception unless __exit__() itself failed.  But
               # throw() has to raise the exception to signal
               # propagation, so this fixes the impedance mismatch
               # between the throw() protocol and the __exit__()
               # protocol.
               #
               if sys.exc_info()[1] is not value:
                   raise

def contextmanager(func):
   def helper(*args, **kwds):
       return GeneratorContextManager(func(*args, **kwds))
   return helper