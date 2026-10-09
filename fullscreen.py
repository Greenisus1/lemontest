import subprocess,sys
from terminal_ui import run
ROWS = [('Run original speedtest (confirmation required)', ['bash', 'lemontest.sh'])]
def session(ui):
 while True:
  n=ui.menu('LemonTest - speedtest accepts Ookla terms; may install packages',[r[0] for r in ROWS]+['Quit'])
  if n is None or n==len(ROWS):return
  if True and not ui.confirm('Continue? This runs the original script with its package/service/terms effects.'):continue
  ui.external(lambda:subprocess.run(ROWS[n][1],check=False))
  ui.message('Original command finished. No success claim is inferred. See its terminal output.')
if __name__=='__main__':raise SystemExit(run('lemontest',session))
