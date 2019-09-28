# Nama (String)
class nama():
    nama = " Name           "
 
    def dataNama(self, argument):
        print(self.nama,'   : Michkail ')
 
nama = nama()
 
nama.dataNama(0);

# Umur (Number)
class umur():
    umur = " Age           "
 
    def dataUmur(self, argument):
        print(self.umur,'    : 23th ')
 
umur = umur()
 
umur.dataUmur(0);

# Alamat (String)
class alamat():
    alamat = " Address           "
 
    def dataAlamat(self, argument):
        print(self.alamat,': Jakarta Timur ')
 
alamat = alamat()
 
alamat.dataAlamat(0);

# Hobi (Array)
hobi=["Drawing", "Reading", "Writing", "Photograph", "Jogging"]
test=["zdd", "zd"]

print (' Hobbies            : 1.',hobi[1])
print ('                      2.',hobi[2])
print (' 	              3.',hobi[3])
print (' 	              4.',hobi[4])
print (' 	              5.',hobi[0])

# is_merried (Boolean)
none = '' 
print(none, 'Is_Merried         :', bool(none)) 

# list_school
nama_lembaga=["Gunadarma", "SMA Bina Dharma", "SMP PGRI 9", "SDN 06"]
year_in=[2002, 2008, 2011, 2014]
year_out=[2008, 2011, 2014, 2019]
major=["A.Md.Kom", "SMA", "SMP", "SD"]

print(' list_school        :', 'Kampus/Sekolah', ' Tahun Masuk', ' Tahun Lulus', '  Gelar')
print('                     ',nama_lembaga[0],'     ',year_in[0],'       ',year_out[0],'        ',major[0])
print('                     ',nama_lembaga[1],year_in[1],'       ',year_out[1])
print('                     ',nama_lembaga[2],'    ',year_in[2],'       ',year_out[2])
print('                     ',nama_lembaga[3],'        ',year_in[3],'       ',year_out[3])

# Skill
skill_name=["PHP", "HTML", "CSS", "Django", "Python", "Query", "Photograph", "JavaScripts"]
level=["Beginner", "Advanced", "Expert"]

print(' Skills             :',skill_name[2],"       ",level[0])
print('                     ',skill_name[3],"    ",level[0])
print('                     ',skill_name[1],"      ",level[1])
print('                     ',skill_name[7],level[0])
print('                     ',skill_name[0],"       ",level[0])
print('                     ',skill_name[4],"    ",level[1])
print('                     ',skill_name[6],"",level[2])
print('                     ',skill_name[5],"     ",level[0])        

# interest_in_coding (Boolean)
none = '' 
print(none, 'interest_in_coding :', bool(1))