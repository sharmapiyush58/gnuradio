try:
    from grc.python.Platform import Platform
except ImportError:
    from gnuradio.grc.python.Platform import Platform


# This class gets all the block keys without generating a flowgraph
class Block_keysget:
    def __init__(self):
        self.platform = Platform()
        block_keys = self.platform.get_block_keys()

def main():
    Block_keysget()

if __name__ == "__main__":
    main()
