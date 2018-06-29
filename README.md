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

![image](https://github.com/410421250/Machine-Learning-Programming-Assignment-2/blob/master/neurons.jpg)

這個實驗中可以觀察到，增加神經元的數目確實是可以增加辨識的強度，但是在到達一個極限後，正確率上升的數目就會趨緩。

5.增加層數
  設定為一層100個神經元，epochs為 10,增加層數來測試強度。
  
  ![image](https://github.com/410421250/Machine-Learning-Programming-Assignment-2/blob/master/layer.jpg)
  
  根據這個實驗，可以看出層數對正確率的影響還是有的，雖然並不明顯，但是我計算每個神經元的總數，發現一層的神經元總數是(784*100+100)+(100*10 10) = 79510及兩層的神經元總數是(784*100+100)+(100*100+100)+(100*10+10) = 89610發現他們都神經元總數只相差12%而已，所以結論是層數要和神經元數目一起看，可以用來判斷增加的強度。
  


