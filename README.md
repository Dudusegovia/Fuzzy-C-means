# Fuzzy-C-means
Algoritmo de classificação soft clustering


> **Resumo:** O Fuzzy C-Means (FCM) é um método de **clustering suave (fuzzy)** no qual **cada amostra pertence a todos os clusters** com **graus de pertinência** em \([0,1]\). Diferente do K-Means (partição dura), o FCM minimiza uma função objetivo que pondera as distâncias aos centróides pelos graus de pertinência elevados a um **fuzzificador** \(m>1\).

---

##  O que é e por que usar

- **Clustering fuzzy:** em vez de rótulos exclusivos, cada ponto \(x_i\) possui um vetor de pertinências \(\mathbf{u}_i = (u_{i1}, \dots, u_{iC})\) tal que \(\sum_{k=1}^{C} u_{ik} = 1\).  
- **Interpretação graduada:** útil quando as fronteiras entre grupos são difusas e faz sentido reportar **incerteza**/ambiguidade (ex.: risco *moderado/alto*).  
- **Parente do K-Means:** recupera um comportamento próximo ao K-Means quando \(m \to 1^+\) (com *hard assignment*).

---
Para cada ponto Xi e cluste j, o peso Wij é inverdamente proporcional à distância xi até o centróide vj, comparada às distâncias até todos os centróides.
<img src="https://av-eks-lekhak.s3.amazonaws.com/media/__sized__/article_images/formula2-thumbnail_webp-600x300.webp">

Atualização dos centróides é descrita por:

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbj6CCMH4QlISqHEm2iKdBasrBbIyyUOr4Zp18tjmNF6JLrtNKH3Wnvs83bHRdB7fEBw&usqp=CAU">


Teste do classificador em um banco de dados de Burnout:


<img width="758" height="474" alt="output" src="https://github.com/user-attachments/assets/c6b3eab6-a8a2-425f-b1f5-0ae477a8c84c" />
<img width="1541" height="574" alt="output4" src="https://github.com/user-attachments/assets/79348cce-42fe-4943-9804-4cda5687102c" />
