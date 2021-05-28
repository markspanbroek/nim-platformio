from os import system

Import("env")

libdeps = env.subst("$PROJECT_LIBDEPS_DIR/$PIOENV")
nimcache = env.subst("$PROJECT_SRC_DIR/nimcache")
main = env.subst("$PROJECT_SRC_DIR/main.nim")
cpu = "avr"
if "espressif" in env.Dump():
    cpu = "esp"

flags = (
    f"--path:{libdeps} "
    f"--nimcache:{nimcache} "
    "--compileOnly "
    f"--cpu:{cpu} "
    "--deadCodeElim "
    "--os:standalone "
    "--noMain "
    "--gc:none "
    "--stacktrace:off "
    "--profiler:off"
)

result = system(f"nim cpp {flags} {main}")
if result != 0:
    exit(result)
