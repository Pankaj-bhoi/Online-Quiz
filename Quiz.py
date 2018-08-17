#Quiz Questions Link " https://www.indiabix.com/current-affairs/international/ "

x = {'This country hosted the communication exercise "Pacific Endeavor-2018 (PE-18)"\nunder the Multinational Communications Interoperability Program (MCIP), recently.'\
     :{1:'South Korea',2:'Nepal',3:'Bangladesh',4:'Pakistan'},
     'Rashida Tlaib set to become the 1st Muslim woman to be elected to the parliament of;'\
     :{1:'Belgium',2:'Switzerland',3:'United States',4:'France'},
     'This country became 3rd Asian nation to get STA 1 status from US.'\
     :{1:'North Korea',2:'Philippines',3:'Indonesia',4:'Afghanistan'},
     'External Affairs Minister Sushma Swaraj and this country minister discussed the bilateral ties on health, tourism, defence and security.'\
     :{1:'Kyrgyzstan',2:'Uzbekistan',3:'Mongolia',4:'Afghanistan'},
     'Which country got warning from UNICEF about the outbreak of cholera ?'\
     :{1:'Pakistan',2:'Yemen',3:'Indonesia',4:'Iran'},
    'India & __________ to cooperate in bamboo sector in Tripura.'\
     :{1:'Russia',2:'Germany',3:'Japan',4:'France'},
     'The US elevated this country\'s status in the export control regime and designated it as a Strategic Trade Authorization-1 (STA-1) country.'\
     :{1:'Japan',2:'South Korea',3:'India',4:'Bangladesh'},
     'With which country India sign Pact on Financial And Technical Cooperation?'\
     :{1:'Germany',2:'Russia',3:'Israel',4:'Swedan'},
     'Invest India and __________ Ministry sSign MoU for Technological Cooperation.'\
     :{1:'UK',2:'UAE',3:'Malaysia',4:'Turkey'},
    'India and __________ signed an MoU to promote investment facilitation.'\
     :{1:'Russia',2:'France',3:'Italy',4:'South Africa'},
     }
y = (2,3,4,1,2,3,3,1,2,2)
index = 0
score = 0
print("Welcome to The Quiz Challenge....")
print('There are 10 Questions... For every Questions contains 50 points..')
print("To proceed...press Enter..")
click = input()

print('The Questions is :')
for i,j in x.items():
    print(i)
    for n,m in j.items():
        print(n,'.',m)
    answer = int(input('Enter Option :'))
    if answer == y[index]:
        print('Correct...')
        score+=50
        index+=1
        print('Score :',score)
    else:
        index+=1
        print('Wrong...')
        print('Score :',score)
if score>=450:
    print("\n")
    print('Excelent...')
    print('\n')
elif score>=300 and score<450:
    print("\n")
    print('Very Good...Not Bad...')
    print('\n')
elif score>=150 and score<300:
    print("\n")
    print('Good..')
    print('\n')
else:
    print("\n")
    print('Better Luck Next Time..')
    print('\n')
            
            
            
        

