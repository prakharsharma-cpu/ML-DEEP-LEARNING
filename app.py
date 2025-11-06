import { useState } from "react";
import { Camera, Recycle, TrendingUp, Leaf } from "lucide-react";
import { Button } from "@/components/ui/button";
import { WasteCategories } from "@/components/WasteCategories";
import { DetectionInterface } from "@/components/DetectionInterface";
import { DetectionResults } from "@/components/DetectionResults";
import { StatsCard } from "@/components/StatsCard";
import { toast } from "sonner";
import heroBg from "@/assets/hero-bg.jpg";

interface Detection {
  class: string;
  confidence: number;
  bbox?: [number, number, number, number];
}

const Index = () => {
  const [detections, setDetections] = useState<Detection[]>([]);
  const [isProcessing, setIsProcessing] = useState(false);

  const handleImageSelect = async (file: File) => {
    setIsProcessing(true);
    
    // Simulate YOLO detection - In production, this would call your YOLO v8 API
    setTimeout(() => {
      const mockDetections: Detection[] = [
        { class: "Plastic Bottle", confidence: 0.95 },
        { class: "Metal Can", confidence: 0.88 },
        { class: "Paper", confidence: 0.92 },
      ];
      
      setDetections(mockDetections);
      setIsProcessing(false);
      toast.success("Image analyzed successfully!");
    }, 2000);

    // TODO: Integrate with YOLO v8 API
    // const formData = new FormData();
    // formData.append('image', file);
    // const response = await fetch('/api/detect', { method: 'POST', body: formData });
    // const result = await response.json();
    // setDetections(result.detections);
  };

  return (
    <div className="min-h-screen bg-background">
      {/* Hero Section */}
      <div 
        className="relative h-[60vh] flex items-center justify-center bg-cover bg-center"
        style={{ backgroundImage: `url(${heroBg})` }}
      >
        <div className="absolute inset-0 bg-gradient-to-b from-black/60 to-black/40" />
        <div className="relative z-10 text-center px-4 max-w-4xl">
          <div className="flex items-center justify-center gap-3 mb-6">
            <Camera className="w-12 h-12 text-primary" />
            <h1 className="text-5xl md:text-6xl font-bold text-white">
              Smart Waste Segregation
            </h1>
          </div>
          <p className="text-xl md:text-2xl text-white/90 mb-8">
            AI-Powered Computer Vision for Smart Cities
          </p>
          <Button 
            size="lg" 
            className="bg-primary hover:bg-primary/90 text-primary-foreground px-8 py-6 text-lg"
            onClick={() => window.scrollTo({ top: window.innerHeight * 0.6, behavior: 'smooth' })}
          >
            Start Detection
          </Button>
        </div>
      </div>

      {/* Stats Section */}
      <div className="max-w-7xl mx-auto px-4 py-12">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
          <StatsCard
            title="Total Detections"
            value={detections.length}
            icon={Camera}
            color="secondary"
          />
          <StatsCard
            title="Accuracy Rate"
            value="94%"
            icon={TrendingUp}
            color="primary"
          />
          <StatsCard
            title="Eco Impact"
            value="High"
            icon={Leaf}
            color="organic"
          />
        </div>

        {/* Waste Categories */}
        <div className="mb-12">
          <h2 className="text-3xl font-bold mb-6 text-center">Waste Categories</h2>
          <WasteCategories />
        </div>

        {/* Detection Interface */}
        <div className="grid md:grid-cols-2 gap-6 mb-12">
          <div>
            <h2 className="text-2xl font-bold mb-4">Upload or Capture</h2>
            <DetectionInterface 
              onImageSelect={handleImageSelect}
              isProcessing={isProcessing}
            />
          </div>
          <div>
            <h2 className="text-2xl font-bold mb-4">Detection Results</h2>
            <DetectionResults 
              detections={detections}
              isProcessing={isProcessing}
            />
          </div>
        </div>

        {/* Info Section */}
        <div className="bg-gradient-to-br from-primary/10 to-secondary/10 rounded-xl p-8 text-center">
          <h3 className="text-2xl font-bold mb-4">Powered by YOLO v8</h3>
          <p className="text-muted-foreground max-w-2xl mx-auto">
            This system uses state-of-the-art YOLO v8 computer vision model to detect and classify 
            waste items in real-time, helping smart cities optimize waste management and promote 
            environmental sustainability.
          </p>
        </div>
      </div>
    </div>
  );
};

export default Index;
