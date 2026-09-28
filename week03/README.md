## Week 03

**What did you change?:** AI'ın verdiği kodda değişken isimlerini inceleyip mantığını anladım, testlerimi yaparak çalıştığından emin oldum.
**Tests:**
1. Ali, Yaş 30, weekend, no -> Beklenen: 250.00 TRY (Standard)
2. Can, Yaş 5, weekend, no -> Beklenen: 0.00 TRY (Free)
3. Zeynep, Yaş 12, weekday, no -> Beklenen: 120.00 TRY (Child) - *Boundary age test (sınır yaş testi)*
**Why does the order of the rules matter?:** Kuralların sırası önemlidir çünkü if/elif yapısında program doğru (True) olan ilk koşulu çalıştırır ve gerisine bakmaz. Eğer Öğrenci (Student) kuralını Çocuk (Child) kuralından önce yazsaydık, 10 yaşındaki öğrenci olan bir çocuk %40 yerine %30 indirim alıp haksızlığa uğrardı.