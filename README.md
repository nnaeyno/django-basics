# django-basics
Django project for TBC Academy x USAID

## Tasks done:
* შექმენით ჯანგოს პროექტი
* გაუშვით დეფაულტ მიგრაციები ბაზაში
* შექმენით სუპერ მომხმარებელი და გაიარეთ ავტორიზაცია ადმინში (nnayeno, 1234)
* შექმნით ორი ახალი აპი(store, order), ახალი აპები დაამატეთ სეთინგებშიც
* თითოეულ აპში შექმნეთი ორ ორი view ( ამ ეტაპზე თავისუფალი ხართ view ების შინაარსში, სასურველია იყოს ლოგიკური)
* ვიუები დააკავშირეთ მთავარ urls.py ში ( თითოეულ აპს უნდა ქონდეს თავისი urls.py)

store აპში განსაზღვრეთ შემდეგი მოდელები: Product, Category
კატეგორიების არქიტექტურა უნდა იყოს ხისებრი, ანუ ერთ კატეგორიას შეიძლება ყავდეს რამდენიმე შვილი კატეგორია. ამ სისტემის 
აწყობა უნდა შეეძლოს ადმინს ადმინ პანელიდან, ანუ კატეგორიის დამტებისას უნდა შეეძლოს კატეგორიის არჩევა, იეარარქიის დონე 
შეზღუდული არ უნდა იყოს.
შესაძლებელი უნდა იყოს პროდუქტის რამდენიმე კატეგორიაში განთავსება
პროდუქტის მოდელს განუსაზღვრეთ სურათის ველი, შესაბამისად მოაწყვეთ სეთინგებიც და url ებიც იმისთვის რომ მედია ფაილის მისამართებმა იმუშაონ ლოკალურად.
სხვა ველები თქვენი სურვილისამებრ შეგიძლიათ დაამატოთ
შექმენით 2 ვიუ და შესაბამისად განუსაზღვრეთ მისამართებიც(urls), ერთი view პასუხისმგებელი უნდა იყოს ყველა კატეგორიის ინფორმაციის დაბრუნებაზე, (კატეგორიას წამოყვეს თავისი მშობელი კატეგორიები, [პირველი დონე]), 
მეორე ვიუმ უნდა დააბრუნოს პროდუქტების სია თავისი კატეგორიებით[უშუალოდ მშობელი კატეგორიები], დაბრუნებული პასუხების ფორმატი უნდა იყოს JSON