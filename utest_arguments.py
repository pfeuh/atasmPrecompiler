#!/usr/bin/python
# -*- coding: utf-8 -*-

from arguments import *

import sys

def write(text):
    sys.stdout.write(str(text))
    
def writeln(text):
    write(text)
    write("\n")

def testException(hook, *hook_args):
    error_triggered = False
    try:
        hook(*hook_args)
    except:
        error_triggered = True
    return error_triggered

def testExceptionCodeLine(code_line, debug=False):
    if debug:
        exec(code_line)
        return True
    error_triggered = False
    try:
        exec(code_line)
    except:
        error_triggered = True
    return error_triggered

def format(text):
    return ["%s"%word.strip() for word in text.split()]

if __name__ == "__main__":

    def utest_ARGUMENT():
        a = ARGUMENT('-Wdef')
        a.set(True)
        assert a.get() == True
        a.reset()
        assert a.get() == False
        a.reset()
        a.set(12)
        assert a.get() == True     
        a.reset()
        assert testException(a.set, ('a'))

        a = ARGUMENT('-ifname', str, check_minus=True, check_file=False)
        assert a.get() == False
        assert a.mustTestFile() == False
        assert a.mustTestMinus() == True
        
        a = ARGUMENT('-ifname', str, check_minus=False, check_file=True)
        assert a.get() == False
        assert a.mustTestMinus() == False
        assert a.mustTestFile() == True
        
        a = ARGUMENT('-ifname', str)
        assert a.get() == False
        assert a.mustTestFile() == False
        assert a.mustTestMinus() == False
        a.reset()
        assert testException(a.set, (12))
        assert testException(a.set, (True))
        a.set('123')
        assert a.get() == '123'
        
        a = ARGUMENT('nb_cols', int)
        assert a.get() == False
        a.reset()
        assert testException(a, (set('123')))
        a.reset()
        a.set(123)
        assert a.get() == 123

        a = ARGUMENT('-rom', bool, family=('-rom', '-ram', '-card'))
        assert a.getFamily() == ('-rom', '-ram', '-card')
        assert testExceptionCodeLine("a = ARGUMENT('-rrm', bool, family=('-rom', '-ram', '-card'))")


    def utest_ARGUMENTS():
        # file monitor.asm should exist
        # file monitor.asmu should NOT exist
        ap = ARGUMENTS(offset=0)
        ap.addArgument(ARGUMENT('-ifname', str, check_file=True))
        ap.parse(('-ifname', 'monitor.asm', 'b', 'c'))
        assert ap.get('-ifname') == 'monitor.asm'
        ap.parse(('-ifname', '"monitor.asm"', 'b', 'c'))
        assert ap.get('-ifname') == 'monitor.asm'
        assert testExceptionCodeLine("ap.parse(('-ifname', 'monitor.asmu', 'b', 'c'))")
        assert testExceptionCodeLine("ap.parse(('b', 'c', '-ifname'))")
        ap.parse(('monitor.asm', '-ifname', 'monitor.asm', 'b', 'c'))
        assert ap.get('-ifname') == 'monitor.asm'
        assert 'monitor.asm' in ap.getRejected()
        assert testExceptionCodeLine("ap.parse(('-ifname', 'monitor.asm', '-ifname', 'monitor.asm', 'b', 'c'))")
        ap.addArgument(ARGUMENT('-ofname', str, check_file=True))
        ap.addArgument(ARGUMENT('taratata', str, check_file=True))
        ap.parse(('taratata', 'monitor.asm', '-ofname', 'monitor.asm', '-ifname', 'monitor.asm', 'b', 'c'))
        assert ap.get('-ifname') == 'monitor.asm'
        assert ap.get('-ofname') == 'monitor.asm'
        assert ap.get('taratata') == 'monitor.asm'
        assert testExceptionCodeLine("assert ap.get('turlututu') == 'monitor.asm'")

        ap = ARGUMENTS(offset=0)
        ap.addArgument(ARGUMENT('-ifname', str, check_file=True, check_minus=True))
        ap.addArgument(ARGUMENT('-ofname', str, check_minus=True))
        ap.addArgument(ARGUMENT('-dfname', str, check_minus=True))
        ap.addArgument(ARGUMENT('-lfname', str, check_minus=True))
        family = ('-ram', '-rom', '-card')
        ap.addArgument(ARGUMENT('-ram', family=family))
        ap.addArgument(ARGUMENT('-rom', family=family))
        ap.addArgument(ARGUMENT('-card', family=family))

        args = format("-ofname -ifname")
        assert testExceptionCodeLine("ap.parse(args)")
        args = format("-ifname -ofname")
        assert testExceptionCodeLine("ap.parse(args)")

        args = format("-rom")
        ap.parse(args)
        assert ap.get('-rom')
        assert not ap.get('-ram')
        assert not ap.get('-card')

        args = format("-ram")
        ap.parse(args)
        assert ap.get('-ram')
        assert not ap.get('-rom')
        assert not ap.get('-card')

        args = format("-ram -rom")
        testExceptionCodeLine("ap.parse(args)")
        args = format("-ram -azerty")
        assert ap.get("-ram") == True
        assert ap.get("-rom") == False
        assert ap.get("-card") == False
        args = format("-rom -azerty")
        ap.parse(args)
        assert ap.get("-rom") == True
        assert ap.get("-ram") == False
        assert ap.get("-card") == False

        args = format("-u u -rom -azerty -u")
        ap.parse(args)
        assert ap.getRejected() == ['-u', 'u', '-azerty', '-u']
        assert ap.get('-rom') == True

        ap = ARGUMENTS(offset=0)
        ap.addArgument(ARGUMENT('-ifname', str))
        ap.addArgument(ARGUMENT('-ofname', str))
        ap.addArgument(ARGUMENT('-dfname', str))
        ap.addArgument(ARGUMENT('-lfname', str))
        ap.addArgument(ARGUMENT('-Wall'))
        ap.addArgument(ARGUMENT('-Wabc'))
        ap.addArgument(ARGUMENT('-Wdef'))
        ap.addArgument(ARGUMENT('-Wghi'))
        ap.addArgument(ARGUMENT('-nb_cols', int, check_minus = 1))
            
        ap.parse(())
        kwds = ap.getArgsDictionary()
        for key in kwds.keys():
            assert kwds[key] == False

        ap = ARGUMENTS(offset=0)
        ap.addArgument(ARGUMENT('-Wall'))
        ap.addArgument(ARGUMENT('-Wabc'))
        ap.addArgument(ARGUMENT('-Wdef'))
        ap.addArgument(ARGUMENT('-Wghi'))
        args = format("-Wall")
        ap.parse(args)
        assert ap.get('-Wall') == True
        assert ap.get('-Wabc') == False
        assert ap.get('-Wdef') == False
        assert ap.get('-Wghi') == False
        args = format("-Wabc")
        ap.parse(args)
        assert ap.get('-Wall') == False
        assert ap.get('-Wabc') == True
        assert ap.get('-Wdef') == False
        assert ap.get('-Wghi') == False
        
        ap = ARGUMENTS(offset=0, warning_all=True)
        ap.addArgument(ARGUMENT('-Wall'))
        ap.addArgument(ARGUMENT('-Wabc'))
        ap.addArgument(ARGUMENT('-Wdef'))
        ap.addArgument(ARGUMENT('-Wghi'))
        args = format("-Wall")
        ap.parse(args)
        assert ap.get('-Wall') == True
        assert ap.get('-Wabc') == True
        assert ap.get('-Wdef') == True
        assert ap.get('-Wghi') == True
        
    utest_ARGUMENT()
    utest_ARGUMENTS()  

    ap = ARGUMENTS(offset=0, warning_all=True)
    ap.addArgument(ARGUMENT('-Wall'))
    ap.addArgument(ARGUMENT('-Wabc'))
    ap.addArgument(ARGUMENT('-Wdef'))
    ap.addArgument(ARGUMENT('-Wghi'))
    args = format("-Wabc")
    ap.parse(args)
    assert ap.get('-Wall') == False
    assert ap.get('-Wabc') == True
    assert ap.get('-Wdef') == False
    assert ap.get('-Wghi') == False
    
    args = format("-Wdef -Wghi")
    ap.parse(args)
    assert ap.get('-Wall') == False
    assert ap.get('-Wabc') == False
    assert ap.get('-Wdef') == True
    assert ap.get('-Wghi') == True
    
    args = format("bla bla bla ...i")
    ap.parse(args)
    assert ap.get('-Wall') == False
    assert ap.get('-Wabc') == False
    assert ap.get('-Wdef') == False
    assert ap.get('-Wghi') == False
    
    args = format("-Wall")
    ap.parse(args)
    assert ap.get('-Wall') == True
    assert ap.get('-Wabc') == True
    assert ap.get('-Wdef') == True
    assert ap.get('-Wghi') == True
    
    
    # TODO: encapsulate exception for testing warning_all





        
    writeln("A L L   T E S T S   P A S S E D  !")    