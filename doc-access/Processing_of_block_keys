import Getting_block_keys

block_keys_get = Getting_block_keys.Block_keysget()
block_keys = block_keys_get.block_keys
for i in range(len(block_keys)):
    if block_keys[i][0:7] == 'analog_' or block_keys[i][0:7] == 'blocks_':
        block_keys[i] = block_keys[i][7:]
    elif block_keys[i][0:9] == 'channels_':
        block_keys[i] = block_keys[i][9:]
    elif block_keys[i][0:8] == 'digital_' or block_keys[i][0:8] == 'trellis_' or block_keys[i][0:8] == 'vocoder_':
        block_keys[i] = block_keys[i][8:]
    elif block_keys[i][0:4] == 'dtv_' or block_keys[i][0:4] == 'fcd_' or block_keys[i][0:4] == 'fec_' or block_keys[i][0:4] == 'fft_':
        block_keys[i] = block_keys[i][4:]
    elif block_keys[i][0:5] == 'noaa_':
        block_keys[i] = block_keys[i][5:]
    elif block_keys[i][0:6] == 'qtgui_' or block_keys[i][0:6] == 'audio_':
        block_keys[i] = block_keys[i][6:]
