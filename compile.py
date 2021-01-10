from os import system
Import("env")

libdeps = env.subst("$PROJECT_LIBDEPS_DIR/$PIOENV")
nimcache = env.subst("$PROJECT_SRC_DIR/nimcache")
main = env.subst("$PROJECT_SRC_DIR/main.nim")

flags = \
  f"--path:{libdeps} "\
  f"--nimcache:{nimcache} "\
  "--compileOnly "\
  "--cpu:avr "\
  "--deadCodeElim "\
  "--os:standalone "\
  "--noMain "\
  "--gc:none "\
  "--stacktrace:off "\
  "--profiler:off"

system(f"nim c {flags} {main}")
