% 测试Rastrigin函数u 差分算法 变1位
clc;clear;close all
tic
N = 100;                          %种群数量
T = 1000;                          %迭代次数
W=10;                                %维数
pjt=0;                            %评价次数
population = -5 + rand(N,W).*10;%生成初始种群
%  pjz=pj(population);
% 调用ras和 Rastrigin都可
% pjz=[];
% for i=1:size(population,1)
%    x=population(i,:);
%    pj=Rastrigin(x);
%    pjz=[pjz;pj];
% end
pjz=ras(population);

% pjz=[];
% for i=1:size(population,1)
%    x=population(i,:);
%    pj=Rosenbrock(x);
%    pjz=[pjz;pj];
% end
% pjz=[];
% for i=1:size(population,1)
%    x=population(i,:);
%    pj=Griewank(x);
%    pjz=[pjz;pj];
% end
pjt=pjt+N;                        %累计评价次数
[z,s]=sort(pjz);                  %对评价值升序排列，返回z和s（s是评价值对应的种群中个体的顺序）
population=population(s,:);       %把原来种群按评价值从小到大排列（按上一语句的s排列）
pjz=z;                            %把返回的z赋为新的（带顺序的评价值）
Bestfi=[pjz(1)];                  %取排序后的评价值中的第一个值为最好的那个
BestS=[population(1,:)];          %去排序后的种群中的第一个个体为最好的那个

t = 1;                            %代数初始化
while t < T
    H_pop = [];                   %生成名为H_pop的空矩阵，存放下列add_up的数值（差分处理后的新种群）
    for i = 1:N
           index = sort(fix(rand(1,3).*(N/2-1)+1));   %生成3个随机数*50，取整，排序
           if index(3)==index(2),index(3)=index(3)+5; %判断第三个和第二个值相不相等，若相等则第三个值加5
           end
           add_up = population(index(1),:) + 0.9*rand(1,W).*(population(index(2),:)-population(index(3),:));
                                                      %差分策略。0.75*rand(1,5)为放缩因子，选择种群中的行数为index(1)+...+，进行处理
       H_pop = [H_pop; add_up];                       %把每个add_up装到矩阵H_pop中，为100*5
    end
 
    V_pop = H_pop;                                    %把H_pop赋给V_pop
    for i = 1:N
          j=randi([1 W],1,1);%生成1-W间的一个数
            if rand < 0.01
                V_pop(i,j) = -5+rand*10;
            end
        
    end                                               % 变异以及对V_pop中的值进行越界处
pjzV=ras(V_pop);
%       pjzV=pj(V_pop);
% pjzV=[];
% for i=1:size(V_pop,1)
%    x=V_pop(i,:);
%    pj=Rosenbrock(x);
%    pjzV=[pjzV;pj];
% end
% % 
%     pjzV=[];
% for i=1:size(V_pop,1)
%    x=V_pop(i,:);
%    pj=Griewank(x);
%    pjzV=[pjzV;pj];
% end
%    pjt=pjt+N;                                         %累计评价次数，调试到此处pjt为200次
%     %画变异种群迭代图
%     axis([-5,5,-5,5]);
%     xlabel('X轴');
%     ylabel('Y轴');
%     title(['迭代次数为t=' num2str(t)]);
%     box on;
%     cla;
%     hold on;
%     plot(V_pop(:,1),V_pop(:,2),'*');
%     frame=getframe(gcf);
%     imind=frame2im(frame);
%     [imind,cm] = rgb2ind(imind,256);
%     if i==1
%          imwrite(imind,cm,'test.gif','gif', 'Loopcount',inf,'DelayTime',1e-4);
%     else
%          imwrite(imind,cm,'test.gif','gif','WriteMode','append','DelayTime',1e-4);
%     end
  
pjz=[pjz;pjzV];                                       %将初始种群的评价值和变异后的评价值组合到一起，现在的piz为200*1 
population=[population;V_pop];                        %把进行元素越界处理后的V_pop和原来种群放在一起
[z,s]=sort(pjz);                                      %对它前2句的pjz排序
population=population(s(1:N),:);                      %取前100个 个体
pjz=z(1:N);                                           %取返回的z中的100个评价值
Bestfi=[Bestfi;pjz(1)];                               %每次评价都挑出最好的 值存放到Bestfi
BestS=[BestS;population(1,:)];                        %每次评价都挑出最好的 个体存放到BestS
% 
% 
%    if t==1
%     subplot(2,2,1)
%     plot(1:N,pjzV,'.r')%画变异种群图，未排序的
%     xlabel('1至100个个体')
%     ylabel('函数值')
%     title('t=1')
%    end
%     if t==40
%     subplot(2,2,2)
%     plot(1:N,pjzV,'.r')%画变异种群图，未排序的
%     xlabel('1至100个个体')
%     ylabel('函数值')
%     title('t=40')
%     end
%     if t==100
%     subplot(2,2,3)
%     plot(1:N,pjzV,'.r')%画变异种群图，未排序的
%     xlabel('1至100个个体')
%     ylabel('函数值')
%     title('t=100')
%     end
  
        t = t + 1;
     if Bestfi(end)<10E-5 
%         subplot(2,2,4)
%          plot(1:N,pjzV,'.r')%终止时
         break
     end                      %按精度要求停止
    
end

population(1:10);%显示种群前10行

     disp(['当前最优解：',num2str(BestS(end,:))]) 

%disp(['程序评价次数：',num2str(pjt)])
disp([num2str(toc)]);
disp([num2str(t)])
disp([num2str(Bestfi(end))]) 





