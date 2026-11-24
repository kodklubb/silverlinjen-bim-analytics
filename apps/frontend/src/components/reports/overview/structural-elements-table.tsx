import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card";

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

import type { StructuralElement } from "@/types/quantities";
import { formatVolume } from "@/utils/formatters";

interface StructuralElementsTableProps {
  elements: StructuralElement[];
}

export function StructuralElementsTable({
  elements,
}: StructuralElementsTableProps) {
  return (
    <Card className="min-w-0 shadow-sm">
      <CardHeader>
        <CardTitle>Structural Elements</CardTitle>

        <CardDescription>
          {elements.length} structural elements extracted
          from the IFC model.
        </CardDescription>
      </CardHeader>

      <CardContent>
        <div className="overflow-x-auto rounded-lg border">
          <Table>
            <TableHeader className="bg-muted/50">
              <TableRow>
                <TableHead>#</TableHead>
                <TableHead>IFC Global ID</TableHead>
                <TableHead>IFC Class</TableHead>
                <TableHead>Name</TableHead>
                <TableHead>Category</TableHead>
                <TableHead>Material</TableHead>

                <TableHead className="text-right">
                  Net Volume (m³)
                </TableHead>
              </TableRow>
            </TableHeader>

            <TableBody>
              {elements.map((element, index) => (
                <TableRow key={element.global_id}>
                  <TableCell className="text-muted-foreground">
                    {index + 1}
                  </TableCell>

                  <TableCell className="font-mono text-xs">
                    {element.global_id}
                  </TableCell>

                  <TableCell>
                    {element.ifc_class}
                  </TableCell>

                  <TableCell>
                    {element.name ?? "—"}
                  </TableCell>

                  <TableCell>
                    {element.category ?? "—"}
                  </TableCell>

                  <TableCell>
                    {element.material ?? "—"}
                  </TableCell>

                  <TableCell className="text-right font-medium tabular-nums">
                    {formatVolume(element.net_volume_m3, 3)}
                  </TableCell>
                </TableRow>
              ))}

              {elements.length === 0 && (
                <TableRow>
                  <TableCell
                    colSpan={7}
                    className="h-24 text-center text-muted-foreground"
                  >
                    No structural elements found.
                  </TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
        </div>
      </CardContent>
    </Card>
  );
}