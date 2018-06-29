# Machine-Learning-Programming-Assignment-2
Handwritten Character Recognition 



1.這次的手寫辨識，我打算用keras來進行辨識，在深度學習中，keras算是一個比較好入門的工具，接下來會使用各種的model模型來進行比較，在可以看出明顯優化的原則下，每一層的神經數量會盡量精簡，來達到這一個目的。

2.優化器的比較
  這次取了五種不同的優化來做比較，分別是RMSprop, SGD, Adagrad, Adam ,Adamax這五種，使用的都是同一個model，都是兩層的Full connected，神經元數都是10個
  ，使用的設備是GTX 1060，batch_size等於100，epochs等於5。
  ![image](https://github.com/410421250/Machine-Learning-Programming-Assignment-2/blob/master/optimizer.jpg)
  
  觀察到這五個優化器所呈現出來的成果，除了SGD的辨識正確率相比之下偏低之外，其他四個的辨識成功率都相差無幾，所以在挑選上，不會選擇SGD來當作優化器。

3.epochs數目的改變
  我們挑選Adam當作我們的優化器。
  ![image](https://github.com/410421250/Machine-Learning-Programming-Assignment-2/blob/master/epochs.jpg)
  
  藉由這張圖可以觀察到，在15 epochs的訓練中，正確率卻沒有明顯的增長，甚至還更低，這有兩個可能性，第一個是因為model產生了overfitting的情況，但是這個問題不太可能，因為這個model的強度設定的很低，所以產生overfitting可能性不大，那麼就是第二種可能，就是因為model的強度實在是太低，到達了這個model的極限了，所以在下一個測試會增加每層神經元的數目來實驗。
  
  
4.增加神經元數目
原本是10個神經元一層，現在用100為倍數來增加並且比較，設定為10 epochs。
