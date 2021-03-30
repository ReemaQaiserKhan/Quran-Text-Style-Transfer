word=("""Sahih International: From among the jinn and mankind."

Pickthall: Of the jinn and of mankind.

Yusuf Ali: Among Jinns and among men.

Shakir: From among the jinn and the men.

Muhammad Sarwar: who induce temptation into the hearts of mankind.

Mohsin Khan: "Of jinns and men."

Arberry: of jinn and men.'
""") 
e=word.split('\n')
q1=e[0].split('Sahih International:') 
q2=e[2].split('Pickthall:') 
q3=e[4].split('Yusuf Ali:') 
q4=e[6].split('Shakir:')
q5=e[8].split('Muhammad Sarwar:')
q6=e[10].split('Mohsin Khan:') 
q7=e[12].split('Arberry:') 
print(q1[1].lstrip(' ')+'\t'+q2[1].lstrip(' '))
print(q1[1].lstrip(' ')+'\t'+q3[1].lstrip(' '))
print(q1[1].lstrip(' ')+'\t'+q4[1].lstrip(' '))
print(q1[1].lstrip(' ')+'\t'+q5[1].lstrip(' ')) 
print(q1[1].lstrip(' ')+'\t'+q6[1].lstrip(' ')) 
print(q1[1].lstrip(' ')+'\t'+q7[1].lstrip(' '))
