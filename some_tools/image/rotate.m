clear all;
clc;

original_img_root='./JPEGImages';
original_xml_root='./Annotations';
rotate_Angle=[90,180,270];


if_90=sum(ismember(rotate_Angle,90));
if_180=sum(ismember(rotate_Angle,180));
if_270=sum(ismember(rotate_Angle,270));
cc=dir([original_img_root,'/*']);
j=1;
for i=1:length(cc)
    if ~(strcmp(cc(i).name,'.'))&&~(strcmp(cc(i).name,'..'))
        ori_img(j).name=cc(i).name;
        j=j+1;
    end
end
clear j

for i=1:length(ori_img)
    if i==34
        aaaaa=2
    end
    name=ori_img(i).name;
    loc_name_point=strfind(name,'.');
    id=name(1:loc_name_point(end)-1);
    xml_name=[id,'.xml'];
    type=name(loc_name_point(end):end);
    image=imread([original_img_root,'/',name]);
    [image_h,image_w]=size(image(:,:,1));
    
    if if_90
        new_image=imrotate(image,90,'loose');
        imwrite(new_image,[original_img_root,'/Angle90_',name]);
        [object,object_num]=read_xml(original_xml_root,xml_name);
        fid=fopen([original_xml_root,'/Angle90_',id,'.xml'],'a');
        new_image_w=image_h;                      %%new size
        new_image_h=image_w;
        firstp=['<annotation> 	<folder>divided_img</folder> 	<filename>',[original_img_root,'/Angle90_',name],'</filename> 	<source> 		<database>remote</database> 		<annotation>remote</annotation> 		<image>flickr</image> 		<flickrid>228217974</flickrid> 	</source> 	<owner> 		<flickrid>hdy</flickrid> 		<name>yangyang</name> 	</owner> 	<size> 		<width>',num2str(new_image_w),'</width> 		<height>',num2str(new_image_h),'</height> 		<depth>3</depth> 	</size> 	<segmented>0</segmented> 	'];
        fprintf(fid,'%s',firstp);
        
        for j=1:length(object)
            xmin=object(j).box(1); 
            ymin=object(j).box(2);
            xmax=object(j).box(3);
            ymax=object(j).box(4);
            new_xmin=ymin;
            new_ymin=image_w-xmax;
            new_xmax=ymax;
            new_ymax=image_w-xmin;
            objp=['<object> 		<name>',object(j).name,'</name> 		<pose>Left</pose> 		<truncated>0</truncated> 		<difficult>0</difficult> 		<bndbox> 			<xmin>',num2str(new_xmin),'</xmin> 			<ymin>',num2str(new_ymin),'</ymin> 			<xmax>',num2str(new_xmax),'</xmax> 			<ymax>',num2str(new_ymax),'</ymax> 		</bndbox> 	</object> 	'];
            fprintf(fid,'%s',objp);
        end
        endp=' </annotation> ';
        fprintf(fid,'%s',endp);
        fclose(fid);
    end
    
    
    if if_180
        new_image=imrotate(image,180,'loose');
        imwrite(new_image,[original_img_root,'/Angle180_',name]);
        [object,object_num]=read_xml(original_xml_root,xml_name);
        fid=fopen([original_xml_root,'/Angle180_',id,'.xml'],'a');
        new_image_w=image_w;              %%new size
        new_image_h=image_h;
        firstp=['<annotation> 	<folder>divided_img</folder> 	<filename>',[original_img_root,'/Angle180_',name],'</filename> 	<source> 		<database>remote</database> 		<annotation>remote</annotation> 		<image>flickr</image> 		<flickrid>228217974</flickrid> 	</source> 	<owner> 		<flickrid>hdy</flickrid> 		<name>yangyang</name> 	</owner> 	<size> 		<width>',num2str(new_image_w),'</width> 		<height>',num2str(new_image_h),'</height> 		<depth>3</depth> 	</size> 	<segmented>0</segmented> 	'];
        fprintf(fid,'%s',firstp);
        
        for j=1:length(object)
            xmin=object(j).box(1); 
            ymin=object(j).box(2);
            xmax=object(j).box(3);
            ymax=object(j).box(4);
            new_xmin=image_w-xmax;
            new_ymin=image_h-ymax;
            new_xmax=image_w-xmin;
            new_ymax=image_h-ymin;
            objp=['<object> 		<name>',object(j).name,'</name> 		<pose>Left</pose> 		<truncated>0</truncated> 		<difficult>0</difficult> 		<bndbox> 			<xmin>',num2str(new_xmin),'</xmin> 			<ymin>',num2str(new_ymin),'</ymin> 			<xmax>',num2str(new_xmax),'</xmax> 			<ymax>',num2str(new_ymax),'</ymax> 		</bndbox> 	</object> 	'];
            fprintf(fid,'%s',objp);
        end
        endp=' </annotation> ';
        fprintf(fid,'%s',endp);
        fclose(fid);
    end
    
    
    
    if if_270
        new_image=imrotate(image,270,'loose');
        imwrite(new_image,[original_img_root,'/Angle270_',name]);
        [object,object_num]=read_xml(original_xml_root,xml_name);
        fid=fopen([original_xml_root,'/Angle270_',id,'.xml'],'a');
        new_image_w=image_h;              %%new size
        new_image_h=image_w;
        firstp=['<annotation> 	<folder>divided_img</folder> 	<filename>',[original_img_root,'/Angle270_',name],'</filename> 	<source> 		<database>remote</database> 		<annotation>remote</annotation> 		<image>flickr</image> 		<flickrid>228217974</flickrid> 	</source> 	<owner> 		<flickrid>hdy</flickrid> 		<name>yangyang</name> 	</owner> 	<size> 		<width>',num2str(new_image_w),'</width> 		<height>',num2str(new_image_h),'</height> 		<depth>3</depth> 	</size> 	<segmented>0</segmented> 	'];
        fprintf(fid,'%s',firstp);
        
        for j=1:length(object)
            xmin=object(j).box(1); 
            ymin=object(j).box(2);
            xmax=object(j).box(3);
            ymax=object(j).box(4);
            new_xmin=image_h-ymax;
            new_ymin=xmin;
            new_xmax=image_h-ymin;
            new_ymax=xmax;
            objp=['<object> 		<name>',object(j).name,'</name> 		<pose>Left</pose> 		<truncated>0</truncated> 		<difficult>0</difficult> 		<bndbox> 			<xmin>',num2str(new_xmin),'</xmin> 			<ymin>',num2str(new_ymin),'</ymin> 			<xmax>',num2str(new_xmax),'</xmax> 			<ymax>',num2str(new_ymax),'</ymax> 		</bndbox> 	</object> 	'];
            fprintf(fid,'%s',objp);
        end
        endp=' </annotation> ';
        fprintf(fid,'%s',endp);
        fclose(fid);
    end
end
