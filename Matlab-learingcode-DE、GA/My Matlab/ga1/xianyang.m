function xianyang
%320085404113
clc;
clear;
%% 参数设置
n=30;                                           %种群个数
w=5;                                            %维数
up=5;ul=-5;                                     %变量上下限
p=(up-ul)*rand(n,w)+ul;                         %种群初始化
yj=pj(p);                                       %对初始种群评价
[yj,d]=sort(yj);                                %评价值排序
p=p(d,:);                                       %对种群排序
%axis([-5,5,-5,5]),plot(p(:,1),p(:,2),'*')      %绘出初始种群分布
xl=1000;                                         %迭代次数
xl0=1;                                          %初始化代数
%% 
while xl0<xl
    for i=1:n
        r1=randi([1,n],1,1);                    %生成一个1-30间均匀分布的随机整数组成的 1×1 列向量
        while (r1==i)
            r1=randi([1,n],1,1);    
        end                                     %while只要相等就继续生成数
        r2=randi([1,n],1,1);
        while (r2==i)||(r1==r2)
            r2=randi([1,n],1,1);
        end
        r3=randi([1,n],1,1);
        while (r3==i)||(r2==r3)||(r1==r3)
            r3=randi([1,n],1,1);
        end                                     %保证r1 r2 r3 i 都不等
        v(i,:)=p(r1,:)+0.8*rand(1,5).*(p(r2,:)-p(r3,:));  %差分策略
    end

        for n=1:n
            for m=1:5
                if rand<0.3 || (v(n,m)<ul)||(v(n,m)>up)%超界的部分换，满足变异概率也换 0.3
                v(n,m)=rand*(up-ul)+ul;
                end
            end
        end
%相当于选择
         pjx=pj(v);                            %对新种群v评价
         pp=[p;v];                             %把新旧种群放在一起
         ppj=[yj;pjx];                         %把评价值放在一起
         [yj,d]=sort(ppj);                     %评价值排序
         p=pp(d(1:n),:);                       %取前30个个体
         yj=yj(1:n);                           %取前30个解      
    xl0=xl0+1;                                 %代数+1 
end
%%
disp(['bestfi:   ',num2str(pp(1,:))])                           %显示最好的个体
disp(['bests:    ',num2str(yj(1))])                              %显示最好的解


