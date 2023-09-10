%遗传算法
clc;clear
%% 参数设置
tic
n=200;                                           %种群个数
w=10;                                            %维数
up=5;ul=-5;                                     %变量上下限
p=(up-ul)*rand(n,w)+ul;                         %种群初始化
% yj=[];
% for i =1:size(p,1)
%     x=p(i,:);
%     gg=Rosenbrock(x);                                       %对初始种群评价
% yj=[yj;gg];
% end
yj=ras(p);   
[yj,d]=sort(yj);                                %评价值排序
p=p(d,:);                                       %对种群排序
T=1000;                                         %迭代次数
t=1;                                          %初始化代数
%% 
by=0.05;                                        %变异概率
while t<T
%% 交叉
    for i=1:n                                   %遍历每个个体
    n1=fix(rand*10)+1;                          %随机选一个个体
    n2=fix(rand*(n-n1))+n1;                     %再随机选一个个体
    alf=rand;                                   %产生一个随机数
    px(i,:)=alf*p(n1,:)+(1-alf)*p(n2,:);        %产生一个新个体
%% 变异
        if rand<by
            m0=rand(1,w)<0.1;                   %产生1行5列的随机数，判断是否小于变异概率，返回一个逻辑数组
            sw=fix(rand*w)+1;                   %在1-5中随机选取一个位置
            m0(sw)=true;                        %如果选取的位置在m0中是1（True）
            m1=(up-ul)*rand(1,w)+ul;            %生成一个m1
            m2=px(i,:);m2(sw)=m1(sw);px(i,:)=m2;
        end
    end
%     pjx=[];
%     for i =1:size(px,1)
%     x=px(i,:);
%     gg=Rosenbrock(x);                                       %对初始种群评价
%     pjx=[pjx;gg];
%     end
    pjx=ras(px);                                 %对新种群进行评价
    pp=[p;px];                                  %初始种群和新种群放在一起
    ppj=[yj;pjx];                               %初始种群和新种群的评价值放在一起
    [yj,d]=sort(ppj);                            %放在一起后排序（升序
    p=pp(d(1:n),:);                             %种群取前30个
    yj=yj(1:n);                                 %评价值取前30个   
        t=t+1;                                  %代数+1
         if yj(end)<10E-5 || t==T

             break
         end                      %按精度要求停止
end

%plot(p(:,1),p(:,2),'r*'),axis([-5,5,-5,5])  %
bestfi=[p(1,:)]%显示个体
bests=[yj(1)];
disp([num2str(toc)]);
disp([num2str(t)])
disp(num2str(yj(1)))%显示值






