import types, sys, traceback
class TestException(Exception): pass
def test(modulename, verbose=None, log=sys.stdout):
    ''' Execute all functions in the named module which have __test__
        in their name and take no arguments.
    modulename:  name of the module to be tested.
    verbose:     If true, print test names as they are executed
    Returns None on success, raises exception on failure.
    '''
    module = __import__(modulename)
    total_tested = 0
    total_failed = 0
    for name in dir(module):
        if '__test__' in name:
            obj = getattr(module, name)
            if (isinstance(obj, types.FunctionType) and
                not obj.func_code.co_argcount):
                if verbose:
                    print>>log, 'Testing %s' % name
                try:
                    total_tested += 1
                    obj()
                except Exception, e:
                    total_failed += 1
                    print>>sys.stderr, '%s.%s FAILED' % (modulename, name)
                    traceback.print_exc()
    message = 'Module %s failed %s out of %s unittests.' % (
               modulename, total_failed, total_tested)
    if total_failed:
        raise TestException(message)
    if verbose:
        print>>log, message
def __test__():
    print 'in __test__'
import pretest
pretest.pretest('microtest', verbose=True)
