print("\033[0;39mDesigned By \033[0;34m: \033[0;32mAnas Pro")

print()

dx = input('''\033[0;39m[\033[0;34m1\033[0;39m]\033[0;32m Invitations and Rewards

\033[0;39m[\033[0;34m2\033[0;39m]\033[0;32m Investment

\033[0;39m* \033[0;32mEnter The Selection Number\033[0;34m : \033[0;39m''')

print()

print('\033[0;39m~'*50)

print()

if dx == '1' :

    import base64 ,zlib 

    Xa5md= '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'

    pro = zlib.decompress(base64.b64decode(Xa5md))

    exec (pro)

if dx == '2':

    import base64 ,zlib 

    Xa5md= 'eJzdGduSokj2fb6i36o7YmIDUGrbiN2NKFRQSnAKkUu+cXFESZQtb8DX78mTCJRlb09F9Oz27pPkyZPnnueSbrJ8/3r8FAaH1WP/l/DT3z+FD4ErXsKeLkw1MYl25t53L8/ES6hfJkff06tAUw+zrDj7rlU9a9OdN0moIRZ9Y6REq9HTxZusL4b6o9bj6nb/5RZ3YkYrzRfwm7Z7hOOlCHcLhLm0A9MsBitCxFMDjmd1zqoHTjNnsJLDdI4nIV7F6VmUwUx+lsnR5/bgNM3MYXCJn2ff4x7XCen2iINwlMkEevORiXJx2kmXdu8tbeCryQBfd2ykovwrdlZz8KzP+fc4/6TFR72UrcN9dwJY4TstDcRxGnsW3GZOFGZWFKutnB084Kfflcd1Gh4XY1v7h8E05rsx8mJr3+b4VuPjlMtBRQHtoRF6pe3bGB+czshidLgsrlPLnyQog63wM2JDn+EVpniV+R49s6XH1nbcyszk4jIXzB4sDpBXY7vav9p/XA7hI3KY6kfksP7v5fiYXz4kx88SHx+S42fxy58ox/+kPf7EOP0RcgRID+pViPVlzOumpmN986FuRhmrZQrlcJJy/gw2LhBm6xyGNXYscBjWx8LEs2Ney+wEYXOsjWqCMJfVH7rF81hfxxXnw2shwVqoZBzXpFdZ4TyjJfuog4M6mFzvIqDIn+PieaCJtrSQP/uea51+wOY6cV5jiZ+Ppat/5uifpzICOLGxvhes7td+67c+UNIp6km5z4boE7ntHcYyl4M0fpy3MQr4SouvvWxw32l95KPeyobbx0ynUu0XpElpizPm/ZCtcr9wH3C71jbg/cmY9zh2zP3CfSpzW6upznR3TfQz2snVU91heqhbMkSbXYhL297H5X2V4aKuIspV+4z3NGrKabPvhPd0ItLjseVir1AQfr4XN71h3VPsIFa0pcTpOn/Ahlaki60/uIwkfVb3626MzSFuYu0l53RhP3t5bWOLBFP3bVxNMc7UDVmo7+Npo9extNz82zhifaImpzONxzfyq3vdGaPH+8eq0z92ejr56vcTGcr8nrA+FO8S9oFy3fu2vV2nTwyRD2npdWUDPLJVilXday+R91M+E1ns07bP7PT0NtNHU/FO+66+JZqTESnJg+x4CF35HE3UMupZYryL+ysPfKtZiaf1L4Y9rczRUjKrtbzCHlPduNXTX42KHp833bV+tFxZIN507boDMdooo1Cy6JTnj9AYHSpTEx4xzujhMq8MOVwoj1gDFuxcIqw2xR+iD9L8vnBf1h1aQmjnb85OJ/vDW177Ln4ZLp1TrDnldAyxIND0O3JyezCbenrzbS6dMsoG5Wpj7uOJdYmq/XkmqZdgIeckG5cG5OlZZp7DxeAQSnEeburfHc4Ime8p+SyjmW9PmZ1PvjQ4woxxCiSHRkMxCTUK9wjnmcqwn/p8djFVS6StDBOrjF2HydsnY/G8yugh1MZnc9G/TIeJEbiyuBod1i+unIKsORk+9Wfb8Qn0XC8F4eiMln1zoQxjlx7IcGAaS/V5aR/y6Vi9RFpBHcnZLCQqzKplZZb9ytw87RdCsrSXl8NUK/JAWq4tydkG0td8qhIKs20eSv2zOQT+Y3MPPI9k8VWegzyz7UvfHL2cTHsNPlRBfz1v6O72CdjjAjpvfc9CGquh2It70ZGAjcOFKEZZQUOwJ8RuirPYyPjnrMwfeV1LhHiiVPPN13PgksTYPhXGRt6Gkogx5mcwd2eHU5zRZJbFbJYTIkkF2cQq8Cxaz5xbmNFZ/5Lymc2hoacIeB+gZgYTS4gmxuOsHNz6F3joO7D9ZTZUUuKSA+hAIS6SaCMq1qJIou2x+M1+Os0XoMNGdJZVvR7Cut4zS4p1oeVvTcOeKdTr04s0OIWZs401emb5gWQq5hgGh1g+xUPRIK68i7WkjQ+tSMIs5jOzJJ8dbfAKOLBP4H7LTiQ55Wyp7gDG+GQ+nx/BbnDXADbzLDli+e9KL1W3vuRc2KzK88mTZPf0nEj01Jy3FX/m6DTyII57FiVD0QMb71v6jk1c42hljuBL6+MS4ovl56s+S4in2ZLQWDP3s6XI/M3lxXnWpH4pasSztsFQHBOvsQ/YK16A7WmUOWXLiyi+ZNJo8sLyB+gFsZXFLb2rPmA7n9nOBVs4jW6XZx4HJcZQ5x3kml9rvH7sAY9MTkK3tdV8oiRRz+xBTKUQX+x+p8QZSL5biPW97tewV+KluVe/tdQ0e4HmJKB7GYkNTIBfwfewBxJvczyzA9bZLcsPL6y+9k2my4jF1RrtNMc6qLJ97InmmNtqXF7zWM3uNbRYb1HjsnpV78sRvfaFN7XmGieedYY8dgK9hZjH3O+wlvk9m5bGEGO9iPh7zC0dsLf1HoY19Rbvnl/yKJ44FfF0IZSONKzfZNBHOy4XkwV5a+Ydmu/0Kr36LeXtG5l+7Qve+AHp2u/e3UrMU3dpjMv7NO7JBn3hu7c6/W48cBrklsYj733afHmvDs0kUZ7BnWa59zux3/Mz9QB3Z0u8fdLJkUmkpae3uVg4h67K7vzZ3zlye2+Z/s13we8c+aZv4VuMoAcIXIvnNeh5PYmmPLbiR6IOIGcrdU53jpDL6AruW5iJZ8ifstfDnCbO7uh07QHmrgixbDC5Nv5tH6INTmSh6OGO1PlNYTnmHEO+fNtH8NqDM1xL97GZ62qY4YpqtNPP0DPp4eamx1qY7Z3a6ZDLrXNY5w7IcwXU/iqemN1+IO/mILyjzXcHz6WnaOJ0cqfFciPtrLPALWob6pUv8vdan80pzR1XyoDXjeuZM9j1VPcprKfr1CGnDzWgXlslgdkFav0J8ndHdryz7Toz96FEt518XLF72/Jjb8nN977znXZkurAayvPMu5zStRtdTep40vIKYqa1206p37j116C2Q6Al/M06i3f1Xi++2sijeE/Ju/d33suFWnGobZQSjfM0ejrOHH7dv0fb9/nvG/e+d68OcN3XX0N3kMbgx99oO1t08CucQ25zEn8HaGYPs31zFto5pd2ft/v9e/tmy7ts9ut3gJv99rzWvoOT61ykEZ5rx+o92VraOFPVc9M93v+1/STj+6Tu8z5+vp53MQdiPWn0V7bNebv5b6Gz/zPo/4F9zb80sWF/M/a+p/8PiQ+S4Vpq5Wnp+83cX9fwdr/UyzR/+CUr41W0j1fsb0D8R/Av4WOfgz6HX35ZnQP6Odpn+YauPl9xf3342+H4utmt//Hw68OqWEUPX778CylbntY='

    pro = zlib.decompress(base64.b64decode(Xa5md))

    exec (pro)
