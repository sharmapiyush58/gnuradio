import Getting_block_keys
import links_list

Block_class = Getting_block_keys.Block_keysget()
all_keys = Block_class.block_keys

all_links = links_list.key_links_refer_dict
all_final_links = []


for i in range(len(all_keys)):
    for j in range(len(all_links)):
        if all_keys[i][0] == all_links.items()[j][0]:
            local_links = []
            for k in range(len(all_links.items()[j][1])):
                local_links.append('http://gnuradio.org/doc/doxygen/search/' + all_links.items()[j][1][k] + '.js')       
            all_final_links.append(local_links)
            break


