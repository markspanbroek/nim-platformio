from os import system, path
from shutil import copyfile
from pathlib import Path

Import("env")

src = Path(env.subst("$PROJECT_SRC_DIR"))

if not path.exists(src/'panicoverride.nim'):
  copyfile(Path().parent/'panicoverride.nim', src/'panicoverride.nim')

libdeps = env.subst("$PROJECT_LIBDEPS_DIR/$PIOENV")

cpu = "avr"
if "espressif" in env.subst("$PIOPLATFORM"):
  cpu = "esp"

flags = (
  f"--path:{libdeps} "
  f"--nimcache:{src/'nimcache'} "
  "--compileOnly "
  f"--cpu:{cpu} "
  "--deadCodeElim "
  "--os:standalone "
  "--noMain "
  "--gc:none "
  "--stacktrace:off "
  "--profiler:off"
)

result = system(f"nim cpp {flags} {src/'main'}")
if result != 0:
  exit(result)
