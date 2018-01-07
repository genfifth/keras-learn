import time, subprocess

def run_tb(logdir, port=6006):
    """
    Run tensorboard on python env.

    # Arguments
    logdir: str
        Tensorboard's log dir.
    port: int
        Tensorboard's tensorboard's listen port.
    """
    subprocess.call("pkill -9 tensorboard", shell=True)
    time.sleep(2)
    subprocess.call("tensorboard --logdir="+logdir+" --port "+str(port)+" &", shell=True)
