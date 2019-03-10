    model_name = 'resnet50'
    model = pretrainedmodels.__dict__[model_name](num_classes=1000, pretrained='imagenet')
    model.avgpool = torch.nn.AdaptiveAvgPool2d((1,1))
    model.last_linear = torch.nn.Linear(in_features=2048, out_features=classes, bias=True)
    #model = v4(num_classes=12)
    model = torch.nn.DataParallel(model).cuda()

    ######### swa
    swa_model = pretrainedmodels.__dict__[model_name](num_classes=1000, pretrained='imagenet')
    swa_model.avgpool = torch.nn.AdaptiveAvgPool2d((1,1))
    swa_model.last_linear = torch.nn.Linear(in_features=2048, out_features=classes, bias=True)
    swa_model = torch.nn.DataParallel(swa_model).cuda()

#### TRAIN
swa_n = 0
for i in range(epoch):
    if swa_flag and epoch >= changepoint[-1]:
    utils.moving_average(swa_model, model, 1.0 / (swa_n + 1))
    utils.bn_update(train_loader, swa_model)
    precision, avg_loss = validate(val_loader, swa_model, criterion)
    with open('./result/%s.txt' % file_name, 'a') as acc_file:
        acc_file.write('Epoch: %2d, train_acc: %.8f, train_loss: %.8f, SWA-Precision: %.8f, SWA-Loss: %.8f, Lr: %.8f\n' % (epoch, train_acc, train_loss, precision, avg_loss, lr))
    swa_n += 1