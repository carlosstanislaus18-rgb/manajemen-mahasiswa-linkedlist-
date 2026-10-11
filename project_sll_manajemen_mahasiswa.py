class Node:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def tambah_awal(self, nim, nama):
        new_node = Node(nim, nama)
        new_node.next = self.head
        self.head = new_node
        print(f"Berhasil tambah {nama} di awal")

    def tambah_akhir(self, nim, nama):
        new_node = Node(nim, nama)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        print(f"Berhasil tambah {nama} di akhir")

    def tampil(self):
        if not self.head:
            print("Data kosong")
            return
        curr = self.head
        print("\n--- Daftar Mahasiswa ---")
        while curr:
            print(f"NIM: {curr.nim} | Nama: {curr.nama}")
            curr = curr.next
        print("------------------------\n")

    def hapus(self, nim):
        if not self.head:
            print("Data kosong")
            return
        if self.head.nim == nim:
            print(f"Hapus {self.head.nama}")
            self.head = self.head.next
            return
        curr = self.head
        while curr.next and curr.next.nim != nim:
            curr = curr.next
        if curr.next:
            print(f"Hapus {curr.next.nama}")
            curr.next = curr.next.next
        else:
            print(f"NIM {nim} tidak ditemukan")

# === TEST PROGRAM ===
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.tambah_akhir("001", "Putri")
    sll.tambah_awal("002", "Sayang Beta")
    sll.tambah_akhir("003", "Budi")
    sll.tampil()
    sll.hapus("002")
    sll.tampil()