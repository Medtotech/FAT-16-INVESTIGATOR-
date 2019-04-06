#Evelyn Okougbo
#10/27/2018
#Assigment 3: Investigating a File System

def file_system():
    
    disk_image = "Image.img"
    with open(disk_image, 'rb') as f:
        
        """Seek offset, read the required number of bytes
        while encoding to hex. convert string to a list
        and swap bytes. Join list back to form a string and
        convert to decimal."""
    
        print "Boot block = 512"
    
        f.seek(0x0B)           
        bytes_per_sector = f.read(2).encode('hex')
        i= list(bytes_per_sector)
        i[0],i[1],i[2],i[3], = i[2],i[3],i[0],i[1]
        bytes_per_sector = ''.join(i)
        bytes_per_sector = int(bytes_per_sector,16)
        print "Number of bytes per sector:",bytes_per_sector

        f.seek(0x0D)
        sector_per_cluster = f.read(1).encode('hex')
        sector_per_cluster= int(sector_per_cluster, 16)
        print  "Number of sectors in each cluster:",sector_per_cluster

        f.seek(0x0E)
        reserved_sectors = f.read(1).encode('hex')
        reserved_sectors= int(reserved_sectors, 16)
        print  "Number of reserved sectors:",reserved_sectors

        f.seek(0x10)
        allocation_table = f.read(1).encode('hex')
        allocation_table= int(allocation_table, 16)
        print "Number of file allocation tables present:",allocation_table

        f.seek(0x11)
        root_directory = f.read(2).encode('hex')
        i= list(root_directory)
        i[0],i[1],i[2],i[3], = i[2],i[3],i[0],i[1]
        root_directory  = ''.join(i)
        root_directory= int(root_directory ,16)
        print  'Max number of entries root directory can hold:',root_directory

        f.seek(0x16)
        copy_of_fat= f.read(2).encode('hex')
        i= list(copy_of_fat)
        i[0],i[1],i[2],i[3], = i[2],i[3],i[0],i[1]
        copy_of_fat = ''.join(i)
        copy_of_fat = int(copy_of_fat,16)

        print "Each file allocation table occupies:",copy_of_fat

       
        """The byte offset where the first FAT begins"""
    
        first_fat = reserved_sectors *bytes_per_sector*sector_per_cluster
        print "The first file allocation table offset is", first_fat
        

        second_fat=  first_fat + bytes_per_sector * copy_of_fat
        print "The byte offset of the second FAT table?",second_fat

        root_dir_entry= second_fat + bytes_per_sector *copy_of_fat
        print "The first byte offset of the  first root directory entry is", root_dir_entry

        
        r_size =root_directory * 32
        first_data_block = r_size+ root_dir_entry
        
        print "The first byte offset of the first  first data block? is", first_data_block

        """To find the Total size of the data region"""
        hex_image = f.read().encode('hex') 
        block= hex_image[first_data_block:len(hex_image)]
        block = len(block) / 2
        print "Total size of the data region:", block
           
file_system()
    

    

    

    

    


    
