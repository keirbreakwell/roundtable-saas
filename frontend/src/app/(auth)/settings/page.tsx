"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

export default function SettingsPage() {
  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">Settings</h1>
      
      <Card>
        <CardHeader>
          <CardTitle>Account Settings</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="space-y-2">
            <label className="text-sm font-medium">Email Address</label>
            <Input type="email" placeholder="your@email.com" disabled />
          </div>
          
          <div className="space-y-2">
            <label className="text-sm font-medium">Organization Name</label>
            <Input placeholder="Your Organization" />
          </div>
          
          <Button>Save Changes</Button>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>API Keys</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="space-y-2">
            <label className="text-sm font-medium">Production API Key</label>
            <Input type="password" value="************************" disabled />
          </div>
          <Button variant="outline">Generate New Key</Button>
        </CardContent>
      </Card>
    </div>
  )
}