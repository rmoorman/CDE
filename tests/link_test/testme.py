import sys
sys.path.insert(0, '..')
from cde_test_common import *

clear_cde_root()

(stdout, stderr) = Popen([CDE_BIN, "python", "link.py"], stdout=PIPE, stderr=PIPE).communicate()
if stderr: print "stderr:", stderr

assert os.path.isfile('cde-root/home/pgbovine/CDE/tests/test_file.txt')
assert os.path.isfile('cde-root/home/pgbovine/CDE/tests/test_file.hardlink')
generic_lib_checks()