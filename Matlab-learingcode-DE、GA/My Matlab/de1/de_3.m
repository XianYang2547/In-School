
% 测试Rastrigin函数 差分算法 个体每一维随机变
clc;clear;close all
tic
N =200;                           %种群数量
T = 1000;                          %迭代次数
W=10;                              %维数
pjt=0;                             %评价次数
population = -5 + rand(N,W).*10;  %生成初始种群
 %population=fix((2*rand-1)*100)*ones(N,W);%	赋初值
 pjz=ras(population);
 
%  pjz=pj(population);
 
%  m=sort(pjz,'descend');
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

pjt=pjt+N;                        
[z,s]=sort(pjz);                  
population=population(s,:);       
pjz=z;                            
Bestfi=[pjz(1)];                  
BestS=[population(1,:)];          
t = 1;                            
while t < T
    H_pop = [];                   
    for i = 1:N
           index = sort(fix(rand(1,3).*(N/2-1)+1));  
           if index(3)==index(2),index(3)=index(3)+5;end 
           add_up = population(index(1),:) + 0.9*rand(1,W).*(population(index(2),:)-population(index(3),:));                                               
       H_pop = [H_pop; add_up];                       
    end
    V_pop = H_pop;                                   
    for i = 1:N
        for j = 1:W
            if rand < 0.05
                V_pop(i,j) = -5+rand*10;
            end
        end
    end                                               

     pjzV=ras(V_pop);
%       pjzV=pj(V_pop);
%     pjzV=[];
% for i=1:size(V_pop,1)
%    x=V_pop(i,:);
%    pj=Rosenbrock(x);
%    pjzV=[pjzV;pj];
% end

%     pjzV=[];
% for i=1:size(V_pop,1)
%    x=V_pop(i,:);
%    pj=Griewank(x);
%    pjzV=[pjzV;pj];
% end
                                        %累计评价次数，调试到此处pjt为200次
    
%% %画变异种群迭代图
%     axis([-5,5,-5,5]);
%     xlabel('X轴');
%     ylabel('Y轴');
%     title(['迭代次数为t=' num2str(t)]);
%     box on;
%     cla;
%     hold on;
%     plot(V_pop(:,1),V_pop(:,2),'*r');
%     pause(0.3)%每代暂停0.3秒来观测
%     frame=getframe(gcf);
%     imind=frame2im(frame);
%     [imind,cm] = rgb2ind(imind,256);
%     if i==1
%          imwrite(imind,cm,'test.gif','gif', 'Loopcount',inf,'DelayTime',1e-4);
%     else
%          imwrite(imind,cm,'test.gif','gif','WriteMode','append','DelayTime',1e-4);
%     end
      
%%     
pjz=[pjz;pjzV];                                       %将初始种群的评价值和变异后的评价值组合到一起，现在的piz为200*1 
population=[population;V_pop];                        %把进行元素越界处理后的V_pop和原来种群放在一起
[z,s]=sort(pjz);                                      %对它前2句的pjz排序
population=population(s(1:N),:);                      %取前100个 个体
 pjz=z(1:N);                                         %取返回的z中的100个评价值 num2str(t) 

 
 if t==200
    axis([-5,5,-5,5]);
    figure(1)

    xlabel('个体的取值范围','FontSize',20);
    ylabel('个体的取值范围','FontSize',20);
    title('迭代终止时','FontSize',20 );
    set(gca,'fontsize',20);%坐标轴字体大小
    set(gca,'XTick',[-5:1:0:1:5]) %¸ %改变x轴坐标间隔显示 这里间隔为1
    set(gca,'YTick',[-5:1:0:1:5]) %¸ %改变x轴坐标间隔显示 这里间隔为1
    box on;
    cla;
    hold on;
    plot(V_pop(:,1),V_pop(:,2),'.k','MarkerSize',15);
    plot(0,0,'*k','MarkerSize',10);legend('个体','原点','FontSize',15);
    set(gca,'linewidth',2)%图周围边框
end



% if t==10
%     axis([-5,5,-5,5]);
%     xlabel('X轴');
%     ylabel('Y轴');
%     title(['迭代次数为t=' num2str(t)]);
% %     box on;
% %     cla;
% %     hold on;
%  figure
%     plot(V_pop(:,1),V_pop(:,2),'*r');
% end
% if t==99
%     population
% end
% % 重置种群
% if t==100
% population=fix((2*rand-1)*100)*ones(N,W);
% pjz=ras(population);
% % pause(3)%画图时在100代时暂停3秒
% end
% if t==107
%     population
% end

Bestfi=[Bestfi;pjz(1)];                               %每次评价都挑出最好的 值存放到Bestfi
BestS=[BestS;population(1,:)];                        %每次评价都挑出最好的 个体存放到BestS

 t = t + 1;
     if Bestfi(end)<10E-5
         
         break
         
     end                      %按精度要求停止||

end

disp(['当前最优解：',num2str(BestS(end,:))]) 
% disp(['程序评价次数：',num2str(pjt)])
disp([num2str(toc)]);%运行时间
disp([num2str(t)])%迭代次数
disp([num2str(Bestfi(end))]) %最小值
% % 取最优解时10个变量的值
% axis([-5,5,-0.1,0.1])
% x=[1 2 3 4 5 6 7 8 9 10];
% % %  hold on
% % %  box on
% % % plot(0,0,'*')
%  plot(x,BestS(end,:),'-k.','linewidth',1,'MarkerSize',30)
% % set(gca,'linewidth',2)
% 
% %     xlabel('FontSize',20);
% %     ylabel('FontSize',20);
%     set(gca,'fontsize',20);%坐标轴字体大小
%     set(gca,'XTick',[0:1:10]) %¸ %改变x轴坐标间隔显示 这里间隔为1
% %     set(gca,'YTick',[-5:1:0:1:5]) %¸ %改变x轴坐标间隔显示 这里间隔为1
% 
% %     plot(V_pop(:,1),V_pop(:,2),'.b','MarkerSize',15);
% %     plot(0,0,'.','MarkerSize',15);legend('个体','原点','FontSize',15);
%     set(gca,'linewidth',2)%图周围边框





