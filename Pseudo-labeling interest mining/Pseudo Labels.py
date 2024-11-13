import torch
import torch.nn.functional as F

#添加一个训练好的模型和未标注数据
model = XXX  #神经网络模型
unlabeled_data = XXX  #未标注的数据集
threshold = 0.9  #可信阈值

pseudo_labels = []  #存储生成的伪标签
selected_samples = []  #存储高置信度样本

#伪标签生成过程
for batch in unlabeled_data:
    inputs = batch["inputs"]  #未标注样本
    outputs = model(inputs)   #模型预测
    probs = F.softmax(outputs, dim=1)  #类别概率分布
    max_probs, pseudo_label = torch.max(probs, dim=1)  #最大概率及对应类别

    #筛选高置信度伪标签
    mask = max_probs > threshold
    selected_samples.append(inputs[mask])  #高置信度样本
    pseudo_labels.append(pseudo_label[mask])  #对应伪标签

#用于后续训练
selected_samples = torch.cat(selected_samples)
pseudo_labels = torch.cat(pseudo_labels)

#定义伪标签损失并进行训练
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters())

for epoch in range(num_epochs):
    optimizer.zero_grad()
    outputs = model(selected_samples)
    loss = criterion(outputs, pseudo_labels)
    loss.backward()
    optimizer.step()
