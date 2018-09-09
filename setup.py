from distutils.core import setup, Extension
import sys

if sys.platform == 'win32':
    extra_compile_args = ['-D_hypot=hypot']
else:
    extra_compile_args = []

hmq_hash_module = Extension(
    'hmq_hash',
    sources=['hmqmodule.cpp', 'sha3/blake.c', 'sha3/bmw.c', 'sha3/groestl.c', 'sha3/jh.c',
             'sha3/keccak.c', 'sha3/skein.c', 'sha3/luffa.c', 'sha3/cubehash.c',
             'sha3/shavite.c', 'sha3/simd.c', 'sha3/echo.c', 'sha3/hamsi.c',
#            'sha3/hamsi_helper.c',
             'sha3/fugue.c', 'sha3/shabal.c', 'sha3/whirlpool.c', 'sha3/sha2big.c', 'sha3/haval.c',
#            'sha3/haval_helper.c',
#            'sha3/aes_helper.c',
#            'sha3/md_helper.c',
             ],
    include_dirs=['.', './sha3'],
    extra_compile_args=extra_compile_args)

setup(name='hmq_hashs',
      version='1.0',
      description='Bindings for proof of work/stake used by hmq',
      ext_modules=[hmq_hash_module])
