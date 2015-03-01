try:
    from grc.python.Platform import Platform
except ImportError:
    from gnuradio.grc.python.Platform import Platform


# This class gets all the block keys without generating a flowgraph and then processes them to make them suitable for searching
class Block_keysget:
    def __init__(self):
        self.platform = Platform()
        self.block_keys = self.platform.get_block_keys()
        block_keys = self.block_keys
        prefixes = ('analog', 'blocks', 'channels', 'digital', 'trellis', 'vocoder', 'dtv', 'fcd', 'fec', 'fft', 'noaa', 'qtgui', 'audio')
        for i in range(len(block_keys)):
            pkey = block_keys[i].partition('_')
            for pre in prefixes:
                if pkey[0] == pre:
                    block_keys[i] = pkey[2]
                    break

        self.block_keys = block_keys

def main():
    Block_keysget()

if __name__ == "__main__":
    main()
