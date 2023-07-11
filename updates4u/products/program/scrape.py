from bs4 import BeautifulSoup
import requests
from products.models import Product
import time

def productcomp(search):
    product_main = []
    finp = search.replace(" ", "+")

    urlm = f"https://www.flipkart.com/search?q={finp}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&sort=popularity&page=" + "1"
    r = requests.get(urlm)

    soup = BeautifulSoup(r.text, "lxml")

    name = soup.find_all("a", class_="s1Q9rs")
    link = soup.find_all("a", class_="s1Q9rs")
    np = soup.find_all("a", class_="_1LKTO3")

    v1name = soup.find_all("a", class_="IRpwTa")
    v1link = soup.find_all("a", class_="IRpwTa")
    v1np = soup.find_all("a", class_="_1LKTO3")

    v3name = soup.find_all("div", class_="_4rR01T")
    v3link = soup.find_all("a", class_="_1fQZEK")
    v3np = soup.find_all("a", class_="_1LKTO3")

    if name:
        for i in name:
            name= i.get("title")

        for i in link:
            name = i.get("href")
            product_main.append(name)

    elif v1name:
        for i in v1name:
            name= i.get("title")

        for i in v1link:
            name = i.get("href")
            product_main.append(name)

    elif v3name:
        for i in v3name:
            name= i.get("title")


        for i in v3link:
            name = i.get("href")
            product_main.append(name)


    else:
        print("Not Matched")

    for i in product_main:
        url= "https://www.flipkart.com" + i
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")
        try:
            name = soup.find("span", class_="B_NuCI").text
        except:
            pass

        try:    
            price = soup.find("div", class_="_30jeq3 _16Jk6d").text
            price = int(price.replace("₹", "").replace(",", ""))

        except:
            pass

        try:
            rev_ratings = soup.find_all("div", class_="_2afbiS")
            try:
                ratings = rev_ratings[0].get_text()
            
            except IndexError:
                pass

            try:    
                ratings = ratings.replace(" Ratings", "").replace(",", "").replace("&", "")
            
            except:
                pass

            try:
                review = rev_ratings[1].get_text()

            except:
                print("Next")
            
            try:
                review = rev_ratings[1].get_text()
                review = review.replace(" Reviews", "").replace(",", "")

            except AttributeError:
                print("Skipping to next product")




        except UnboundLocalError and IndexError:
            try:
                print("Trying diffrent method")
                rev_ratings = soup.find("span", class_="_2_R_DZ _2IRzS8").text
                rev_ratings = rev_ratings.split("and")
                ratings = int(rev_ratings[0].replace(" ratings", "").replace(",",""))
                review = int(rev_ratings[1].replace(" reviews", "").replace(",","").replace(" ", ""))
                print("Done with alternate try")

            except:
                pass


        try:
            overall_rating = float(soup.find("div", class_="_3LWZlK _138NNC").text)

        except AttributeError:
            try:
                overall_rating = float(soup.find("div", class_="_2d4LTz").text)

            except AttributeError:
                pass

        try:
            image_link = soup.find("img", class_="_2r_T1I _396QI4")

            image_link = image_link.get("src")

        except AttributeError:
            try:
                image_link = soup.find("img", class_="_386cs4 _2amPTt _3qGmMb")
                image_link = image_link.get("src")
            
            except:
                image_link = soup.find("img", class_="_396cs4 _2amPTt _3qGmMb")
                image_link = image_link.get("src")




        if int(overall_rating) >= 4 and int(ratings) >= 500 and int(review) >= 10:
            try:
                pname = Product.objects.get(product_name = name)
                print(f" {pname} is already in database")

            
            except:
                print("step2")
                reviewPercent = recomCalc(url)
                product = Product(
                    product_name=name, 
                    price=int(price), 
                    ratings=int(ratings), 
                    reviews=int(review), 
                    overall_ratings = float(overall_rating), 
                    link=url, 
                    img_link=image_link, 
                    query = search, 
                    prating=reviewPercent[0],
                    nrating=reviewPercent[1],
                    )
                product.save()
                print("Successfully Fetched and Saved")


def flipkartProUp(link, id):
    headers={'Cache-Control': 'no-cache, must-revalidate'}
    r = requests.get(link.format(rn=time.time()), headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    try:
        try:
            name = soup.find("span", class_="B_NuCI").text

        except:
            error = "Product Not Found"
            return error

        try:    
            price = soup.find("div", class_="_30jeq3 _16Jk6d").text
            price = int(price.replace("₹", "").replace(",", ""))

        except:
            print("Price not Found")
            price = 0

        try:
            rev_ratings = soup.find_all("div", class_="_2afbiS")

            try:
                ratings = rev_ratings[0].get_text()
            
            except IndexError:
                print("Trying Different Method")

            try:    
                ratings = ratings.replace(" Ratings", "").replace(",", "").replace("&", "")
            
            except:
                print("Trying different Method")

            try:
                review = rev_ratings[1].get_text()

            except:
                print("Next")
            
            try:
                review = rev_ratings[1].get_text()
                review = review.replace(" Reviews", "").replace(",", "")

            

            except AttributeError:
                print("Review and Rating Error")


        except UnboundLocalError and IndexError:
            try:
                print("Trying diffrent method")
                rev_ratings = soup.find("span", class_="_2_R_DZ _2IRzS8").text
                rev_ratings = rev_ratings.split("and")
                ratings = int(rev_ratings[0].replace(" ratings", "").replace(",",""))
                review = int(rev_ratings[1].replace(" reviews", "").replace(",","").replace(" ", ""))
                print("Done with alternate try")

            except:
                ratings=0
                review = 0


        try:
            overall_rating = float(soup.find("div", class_="_3LWZlK _138NNC").text)

        except AttributeError:
            try:
                overall_rating = float(soup.find("div", class_="_2d4LTz").text)

            except AttributeError:
                overall_rating = 0.0

        try:
            image_link = soup.find("img", class_="_2r_T1I _396QI4")

            image_link = image_link.get("src")

        except AttributeError:
            try:
                image_link = soup.find("img", class_="_386cs4 _2amPTt _3qGmMb")
                image_link = image_link.get("src")
            
            except:
                image_link = soup.find("img", class_="_396cs4 _2amPTt _3qGmMb")
                image_link = image_link.get("src")

        try:
            reviewPercent = recomCalc(link)
            print(review)
        except:
            print("error review")
            pass

        pname = Product.objects.get(id = id)
        pname.product_name=name
        pname.price=int(price)
        pname.ratings=int(ratings)
        pname.reviews=int(review)
        pname.overall_ratings = float(overall_rating)
        pname.img_link=image_link
        pname.prating = reviewPercent[0]
        pname.nrating = reviewPercent[1]
        pname.save(update_fields=['product_name', 'price', 'ratings', 'reviews', 'overall_ratings', 'img_link', 'prating', 'nrating'])
        print(reviewPercent)
    except:
        print("error")
        error = "error"
        pass

    return link



def recomCalc(link):
    headers={'Cache-Control': 'no-cache, must-revalidate'}
    r = requests.get(link.format(rn=time.time()), headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    word = "product-reviews"
    reviews = soup.find_all("a", class_=None)
    for r in reviews:
        rlink =  r.get('href')
        print("this is" + rlink)
        if word in rlink:
            rlink = "https://www.flipkart.com" + rlink
            headers={'Cache-Control': 'no-cache, must-revalidate'}
            r = requests.get(rlink.format(rn=time.time()), headers=headers)
            soup = BeautifulSoup(r.text, "lxml")
            word = "product-reviews"
            reviews = soup.find_all("div", class_="_1uJVNT")
            onestar = int(reviews[0].get_text().replace(",", ""))
            twostar = int(reviews[1].get_text().replace(",", ""))
            threestar = int(reviews[2].get_text().replace(",", ""))
            fourstar = int(reviews[3].get_text().replace(",", ""))
            fivestar = int(reviews[4].get_text().replace(",", ""))
            total = onestar + twostar + threestar + fourstar + fivestar
            postiveRecom = ((onestar + twostar) / total) * 100
            negeativeRecom = ((threestar + fourstar + fivestar) / total) * 100
            if negeativeRecom < 50:
                negeativeRecom = negeativeRecom + 1

            if postiveRecom < 50:
                postiveRecom = postiveRecom + 1
            recomm = [int(postiveRecom), int(negeativeRecom)]
            return recomm

    return recomm


# link = "https://www.flipkart.com/godrej-genteel-top-load-front-fresh-liquid-detergent/p/itmd426a23b95c27?pid=LDTETGUWHHFRRZUU&lid=LSTLDTETGUWHHFRRZUU1B3QIA&marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_740b6e81-b877-419b-8c4f-b7f05c010abb_41_OXUV7MV9GM2T_MC.LDTETGUWHHFRRZUU&otracker=clp_basket_pmu_Household%2BCare_3_41.cartPMU.BASKET_PMU_grocery-supermart-store_LDTETGUWHHFRRZUU&otracker1=clp_basket_pmu_PINNED_neo%2Fmerchandising_Household%2BCare_HORIZONTAL_GRID_VIEW_productCard_cc_3_NA_view-all&cid=LDTETGUWHHFRRZUU"
# result = recomCalc(link)
# print(result)



def amazonscript(search):
    pass

def meshoscript(search):
    product_main = []


    finp = search.replace(" ", "+")

    i = 0
    i = i+1

    print(f"Page {i}")
    urlm = f"https://www.amazon.in/s?k={finp}&ref=nb_sb_noss"
    r = requests.get(urlm)
    print(urlm)

    soup = BeautifulSoup(r.text, "lxml")
    

    links = soup.find_all("div", class_="sc-hLBbgP")
    link = links.get("href")
    product_main.append(link)
    np = soup.find_all("a", class_="_1LKTO3")





def ajioscript(search):
    pass

def myntrascript(search):
    pass