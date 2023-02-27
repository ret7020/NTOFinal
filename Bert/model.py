import torch
import torch.nn as nn
import torchvision.models as models

class VideoQANet(nn.Module):
    def __init__(self, video_feature_size, question_feature_size, num_classes):
        super(VideoQANet, self).__init__()
        
        # Video Feature Extraction
        self.cnn = models.video.r3d_18(pretrained=True)
        self.avg_pool = nn.AdaptiveAvgPool3d((1, 1, 1))
        self.fc_video = nn.Linear(video_feature_size, question_feature_size)

        # Question Feature Extraction
        self.bert = BertModel.from_pretrained('bert-base-uncased')

        # Combining Features
        self.fc_combined = nn.Linear(video_feature_size + question_feature_size, num_classes)

    def forward(self, video_frames, question_tokens):
        # Video Feature Extraction
        video_features = self.cnn(video_frames)
        video_features = self.avg_pool(video_features)
        video_features = video_features.view(video_features.size(0), -1)
        video_features = self.fc_video(video_features)

        # Question Feature Extraction
        question_features = self.bert(question_tokens)

        # Combining Features
        combined_features = torch.cat((video_features, question_features), dim=1)
        output = self.fc_combined(combined_features)

        return output

