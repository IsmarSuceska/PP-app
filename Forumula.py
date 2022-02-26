used_goods{'Products1':255.2,'Products2':421.22,'Product3':982.21}

.

desired_products=input('Koji proizvod zelite ?')

if desired_products in used_goods):
    x=((used_goods[desired_products]))
    euros = float(x)
    bam = euros * 1.95583

    print('RRP price is', format(bam, ".2F"))

    outlet = (bam * 1.17) * 0.50
    outlet2 = (bam * 1.17) * 0.25


    print('Discount 1', format(outlet, ".2F"))
    print('Discount 2', format(outlet2, ".2F"))


else:
    print('Product is not correct ')

    for products in used_goods:
         print(products)
