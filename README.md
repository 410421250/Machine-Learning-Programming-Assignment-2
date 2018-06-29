# Machine-Learning-Programming-Assignment-2
Handwritten Character Recognition 



1.這次的手寫辨識，我打算用keras來進行辨識，在深度學習中，keras算是一個比較好入門的工具，接下來會使用各種的model模型來進行比較，在可以看出明顯優化的原則下，每一層的神經數量會盡量精簡，來達到這一個目的。

2.優化器的比較
  這次取了五種不同的優化來做比較，分別是RMSprop, SGD, Adagrad, Adam ,Adamax這五種，使用的都是同一個model，都是Full connected兩層，神經元數都是10個
  ，使用的設備是GTX 1060，batch_size等於100，epochs等於5。
3.
