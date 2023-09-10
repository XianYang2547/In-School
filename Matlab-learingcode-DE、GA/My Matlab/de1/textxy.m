function textxy
% 测试Rastrigin函数 差分算法 个体每一维随机变
clc;clear;close all
tic
N = 100;                           %种群数量
T = 1000;                          %迭代次数
W=10;                              %维数
pjt=0;                             %评价次数
 population = -5 + rand(N,W).*10;  %生成初始种群         法 1
 %population=fix((2*rand-1)*100)*ones(N,W);%	赋初值   法2
pjz=ras(population);
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
    pjt=pjt+N;                                       
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
pjz=[pjz;pjzV];                                      
population=[population;V_pop];                      
[z,s]=sort(pjz);                                     
population=population(s(1:N),:);                     
pjz=z(1:N);                                           
% if t==99
%     population
% end
% if t==100 %在100代时重置种群           可注释掉
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
end
function s = ras(pop)
    % pop = max(-5.12,min(5.12,pop));
    s=10*size(pop,2)+sum(pop.^2 -10*cos(2*pi.*pop),2);
end
% function DrawRastrigin()
%     % 绘制2维Rastrigin函数图形
%     x = [-5 : 0.05 : 5 ];
%     y = x;
%     [X,Y] = meshgrid(x,y);
%     [row,col] = size(X);
%     for  l = 1 :col
%          for  h = 1 :row
%             z(h,l) = ras([X(h,l),Y(h,l)]);
%         end
%     end
%     
%     figure
%     mesh(X,Y,z)
%     hold on
%     contour(X,Y,z)
%     shading interp
% end




