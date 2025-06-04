from flask import Flask, request, jsonify
import torch
import trimesh
from pointnet_model import PointNet

app = Flask(__name__)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = PointNet(output_dim=3).to(device)
model.load_state_dict(torch.load('pointnet_model.pth', map_location=device))
model.eval()

def load_pointcloud(file_path, num_points=1024):
    mesh = trimesh.load(file_path)
    points, _ = trimesh.sample.sample_surface(mesh, num_points)
    return points

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    file_path = 'temp.stl'
    file.save(file_path)

    points = load_pointcloud(file_path)
    points = torch.tensor(points, dtype=torch.float32).unsqueeze(0).transpose(2,1).to(device)

    with torch.no_grad():
        pred = model(points).squeeze().cpu().numpy()

    result = {
        "max_load_N": float(pred[0]),
        "max_speed_kmh": float(pred[1]),
        "drag_coefficient": float(pred[2])
    }
    return jsonify(result)

@app.route('/')
def index():
    return 'PointNet 3D AI API: Use POST /predict'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
