    def mixup_data(x, y, alpha=1.0, use_cuda=True):
        '''Returns mixed inputs, pairs of targets, and lambda'''
        if alpha > 0:
            lam = np.random.beta(alpha, alpha)
        else:
            lam = 1

        batch_size = x.size()[0]
        if use_cuda:
            index = torch.randperm(batch_size).cuda()
        else:
            index = torch.randperm(batch_size)

        mixed_x = lam * x + (1 - lam) * x[index, :]
        y_a, y_b = y, y[index]
        return mixed_x, y_a, y_b, lam


    def mixup_criterion(criterion, pred, y_a, y_b, lam):
        return lam * criterion(pred, y_a) + (1 - lam) * criterion(pred, y_b)



    def train(train_loader, model, criterion, optimizer, epoch):
        batch_time = AverageMeter()
        data_time = AverageMeter()
        losses = AverageMeter()
        acc = AverageMeter()

        # switch to train mode
        model.train()

        end = time.time()
        # 从训练集迭代器中获取训练数据
        for i, (images, target) in enumerate(train_loader):
            # 评估图片读取耗时
            data_time.update(time.time() - end)
            # 将图片和标签转化为tensor
            image_var = torch.tensor(images).cuda(async=True)
            label = torch.tensor(target).cuda(async=True)
            inputs, targets_a, targets_b, lam = mixup_data(image_var, label,
                                                           alpha, True)
            inputs, targets_a, targets_b = map(Variable, (inputs,
                                                          targets_a, targets_b))
            y_pred = model(inputs)
            loss = mixup_criterion(criterion, y_pred, targets_a, targets_b, lam)
            # 将图片输入网络，前传，生成预测值
            #y_pred = model(image_var)
            # 计算loss
            #loss = criterion(y_pred, label)
            losses.update(loss.item(), images.size(0))

            # 计算top1正确率
            prec, PRED_COUNT = accuracy(y_pred.data, target, topk=(1, 1))
            acc.update(prec, PRED_COUNT)

            # 对梯度进行反向传播，使用随机梯度下降更新网络权重
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # 评估训练耗时
            batch_time.update(time.time() - end)
            end = time.time()

            # 打印耗时与结果
            if i % print_freq == 0:
                print('Epoch: [{0}][{1}/{2}]\t'
                      'Time {batch_time.val:.3f} ({batch_time.avg:.3f})\t'
                      'Data {data_time.val:.3f} ({data_time.avg:.3f})\t'
                      'Loss {loss.val:.4f} ({loss.avg:.4f})\t'
                      'Accuray {acc.val:.3f} ({acc.avg:.3f})'.format(
                    epoch, i, len(train_loader), batch_time=batch_time, data_time=data_time, loss=losses, acc=acc))
        return acc.avg, losses.avg