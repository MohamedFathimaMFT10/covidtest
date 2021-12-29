#Mohamed fathima FT10

def convertYNtoBoolean (li):
  for i in range(len(li)):
      if(li[i]=='y' or li[i]=='Y'
         li[i]=True
       elif(li[i]== 'n' or li[i]=='N'):
            li[i]=False
       else:
            li[i]=False
   return li
   #end
         
 def intro():
     return'''
     INSTRUCTIONS :
     ------------
     The input option will be shown.
     give Y/y for yes
     give N/n for no
     for inputs.
     ...
     #end
     
 def displayInformation():
     return'''
         INFORMATION :
         -----------
         *PCR : Polymerase chain reaction, Detect genetic material from a
                specific organisim like virus. This can be a nasal swab or a bit of salaiva.
         *Serious Symptoms :
            *Difficult breating or shortness of breath
            *Loss of speech or mobility, or confusion
            *chest pain
         *Most common symptoms :
            *fever
            *Cough
            *Tiredness
            *Loss of taste or smell
    '''
    #end
    
    def seriousSymptomsInput():
        result = [False,False,False]
        print("----------------------------------------------------")
        result[0] = input( " [1] Difficult breating or shortness of breath : ")
        result[1] = input( " [2] Loss of speech or mobility, or confusion  : ")
        result[2] = input( " [3] chest pain                                : ")
        result = convertYNtoBoolean(result)
        return result
        #end
        
   def mostCommonSymptomsInput():
       result =[False,False,False,False]
       print("----------------------------------------------------------")
       result[0] = input( " [1] fever                       : " )
       return[1] = input( " [2] cough                       : " )
       return[2] = input( " [3] Tiredness                   : " )
       return[3] = input( " [4] Loss of taste or smell      : " )
       result = convertYNtoBoolean(result)
       return result
       # end
       
 #main code
 print(displayInformation())
 print(intro))
 
 symptom1 = seiousSymptomsInput()
 symptom2 = mostCommonSymptomsInput()
 
 symptomicResult = "negative"
 # checking symptom1
 # If one symptom occur then three is high possibility of covid 19
 if symptom1[0] or symptom[1] or symptom[2] :
    symptomicResult = "positive"
 elif symptom2[0] and symptom2[1] or symptom2[2]  and symptom2[3]:
     symptomicResult = "positive"
     
     
print("---------------------------------------------------------")
asymtomatic = input("[1] PCR test result : ")

if asymptomatic =='y' or asymptomatic == 'y' :
    print(" (Asymptomatic) Covid positive")
else:
    print(" (Asymptomatic) Covid negative") 
    
print("( Symptomatic) Covid" + symptomaticResult)    
    
 
   
       
