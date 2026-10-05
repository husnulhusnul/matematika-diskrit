python = {"husnul", "lutfia", "tiara"}
java = {"lutfia", "bila"}
sql = {"husnul", "bila", "nizi"}
semua_mahasiswa = {"husnul", "lutfia", "tiara", "bila", "nizi", "suri"}

python_saja = python - (java | sql)
python_dan_java = python & java
minimal_satu = python | java | sql
tidak_menyukai_ketiganya = semua_mahasiswa - (python | java | sql)

print("Python saja:", python_saja)
print("Python dan Java:", python_dan_java)
print("Minimal satu teknologi:", minimal_satu)
print("Tidak menyukai ketiganya:", tidak_menyukai_ketiganya)